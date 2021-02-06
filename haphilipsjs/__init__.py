from typing import Any, Dict, Optional, TypeVar, cast
import requests
from requests.auth import HTTPDigestAuth
import logging
import warnings
import urllib3
from secrets import token_bytes, token_hex
from base64 import b64decode, b64encode

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hmac import HMAC

from .typing import ActivitesTVType, ApplicationIntentType, ApplicationsType, ChannelDbTv, ChannelListType, ChannelType, ChannelsCurrentType, ChannelsType, SystemType

LOG = logging.getLogger(__name__)
TIMEOUT = 5.0
DEFAULT_API_VERSION = 1

AUTH_SHARED_KEY = b64decode("ZmVay1EQVFOaZhwQ4Kv81ypLAZNczV9sG4KkseXWn1NEk6cXmPKO/MCa9sryslvLCFMnNe4Z4CPXzToowvhHvA==")
"""Key used for hmac signatures and decoding of cbc data."""


def hmac_signature(key: bytes, timestamp: str, data: str):
    """Calculate a timestamped signature."""
    hmac = HMAC(key, SHA256())
    hmac.update(timestamp.encode("utf-8"))
    hmac.update(data.encode("utf-8"))
    return b64encode(hmac.finalize()).decode("utf-8")

def cbc_decode(key: bytes, data: str):
    """Decoded encrypted fields based on shared key."""
    raw = b64decode(data)
    assert len(raw) >= 16
    decryptor = Cipher(algorithms.AES(key[0:16]), modes.CBC(raw[0:16])).decryptor()
    unpadder = PKCS7(128).unpadder()
    result = decryptor.update(raw[16:]) + decryptor.finalize()
    result = unpadder.update(result) + unpadder.finalize()
    return result.decode("utf-8")

def cbc_encode(key: bytes, data: str):
    """Decoded encrypted fields based on shared key."""
    raw = data.encode("utf-8")
    iv = token_bytes(16)
    encryptor = Cipher(algorithms.AES(key[0:16]), modes.CBC(iv)).encryptor()
    padder = PKCS7(128).padder()
    result = padder.update(raw) + padder.finalize()
    result = encryptor.update(result) + encryptor.finalize()
    return b64encode(iv + result).decode("utf-8")

class ConnectionFailure(Exception):
    pass

class PairingFailure(Exception):
    def __init__(self, data):
        super().__init__(f"Failed to start pairing: {data}")
        self.data = data

class NoneJsonData(Exception):
    def __init__(self, data):
        super().__init__(f"Non json data received: {data}")
        self.data = data
    """API Returned non json data when json was expected."""


T = TypeVar('T') 

class PhilipsTV(object):

    def __init__(self, host=None, api_version=DEFAULT_API_VERSION, secured_transport=None, username=None, password=None, verify=False, auth_shared_key=None):
        self._host = host
        self._connfail = 0
        self.api_version = int(api_version)
        self.on = False
        self.name: Optional[str] = None
        self.system: Optional[SystemType] = None
        self.min_volume = None
        self.max_volume = None
        self.volume = None
        self.muted = None
        self.sources = None
        self.source_id = None
        self.channels: Optional[ChannelsType] = None
        self.channel_id: Optional[str] = None
        self.applications: Optional[ApplicationsType] = None
        self.application: Optional[ApplicationIntentType] = None
        if auth_shared_key:
            self.auth_shared_key = auth_shared_key
        else:
            self.auth_shared_key = AUTH_SHARED_KEY

        if secured_transport is None:
            secured_transport = api_version == 6
        
        if secured_transport:            
            self.protocol = "https"
            self.port = 1926
        else:
            self.protocol = "http"
            self.port = 1925

        adapter = requests.sessions.HTTPAdapter(pool_connections=1, pool_maxsize=1, pool_block=True)
        self.session = requests.Session()
        self.session.verify=False
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers["Accept"] = "application/json"

        self.session.verify = verify
        if username:
            self.session.auth = HTTPDigestAuth(username, password)

    @property
    def pairing_type(self):
        if self.system:
            return self.system.get("featuring", {}).get("systemfeatures", {}).get("pairing_type")
        else:
            return None

    def _url(self, path):
        return '{0}://{1}:{2}/{3}/{4}'.format(
            self.protocol,
            self._host,
            self.port,
            self.api_version,
            path
        )

    def _getReq(self, path) -> Optional[Dict]:

        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)
                with self.session.get(self._url(path), timeout=TIMEOUT) as resp:
                    if resp.status_code != 200:
                        return None
                    return resp.json()
        except requests.exceptions.RequestException as err:
            raise ConnectionFailure(str(err)) from err


    def _postReq(self, path: str, data: Dict) -> bool:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)

                with self.session.post(self._url(path), json=data, timeout=TIMEOUT) as resp:
                    if resp.status_code == 200:
                        LOG.debug("Post succeded: %s", resp.text)
                        return True
                    else:
                        LOG.warning("Failed to post request: %s", resp.text)
                        return False
        except requests.exceptions.RequestException as err:
            raise ConnectionFailure(str(err)) from err

    def pairRequest(self, app_id: str, app_name: str, device_name: str, device_os: str, type: str, device_id: Optional[str] = None):
        """Start up a pairing request."""
        if device_id is None:
            device_id = token_hex(16)

        device = {
            "device_name": device_name,
            "device_os": device_os,
            "type" : type,
            "id": device_id,
            "app_id": app_id,
            "app_name": app_name,
        }

        state = {
            "device": device
        }

        data = {
            "scope" : [
                "read",
                "write",
                "control"
            ],
            "device": device
        }

        LOG.debug("pair/request request: %s", data)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)

            with self.session.post(self._url("pair/request"), json=data, auth=None) as resp:
                if not resp.headers['content-type'].startswith("application/json"):
                    raise NoneJsonData(resp.text)
                data_response = resp.json()

        LOG.debug("pair/request response: %s", data_response)
        if data_response.get("error_id") != "SUCCESS":
            raise PairingFailure(data_response)

        state["timestamp"] = data_response["timestamp"]
        state["auth_key"] = data_response["auth_key"]

        return state

    def pairGrant(self, state: Dict[str, Any], pin: str):
        """Finish a pairing sequence"""
        auth_handler = HTTPDigestAuth(
            state["device"]["id"],
            state["auth_key"]
        )

        signature = hmac_signature(
            self.auth_shared_key,
            str(state['timestamp']),
            pin
        )

        auth = {
            "auth_appId" : "1",
            "auth_timestamp": state["timestamp"],
            "auth_signature": signature,
            "pin": pin,
        }

        data = {
            "auth": auth,
            "device": state["device"]
        }

        LOG.debug("pair/grant request: %s", data)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)

            with self.session.post(self._url("pair/grant"), json=data, auth=auth_handler) as resp:
                if not resp.headers['content-type'].startswith("application/json"):
                    raise NoneJsonData(resp.text)
                data_response = resp.json()
                LOG.debug("pair/grant response: %s", data_response)

        if data_response.get("error_id") != "SUCCESS":
            raise PairingFailure(data_response)

        self.session.auth = auth_handler
        return state["device"]["id"], state["auth_key"]


    def update(self):
        try:
            if not self.on:
                self.getSystem()

            if not self.on:
                self.getSources()

            if not self.on:
                self.getChannels()

            if not self.on:
                self.getApplications()

            self.getPowerState()
            self.getAudiodata()
            self.getSourceId()
            self.getChannelId()
            self.getApplication()
            self.on = True
            return True
        except ConnectionFailure as err:
            LOG.debug("Exception: %s", str(err))
            self.on = False
            return False

    def _decodeSystem(self, system) -> SystemType:
        result = {}
        for key, value in system.items():
            if key.endswith("_encrypted"):
                result[key[:-10]] = cbc_decode(self.auth_shared_key, value)
            else:
                result[key] = value
        return cast(SystemType, result)

    def getSystem(self):
        r = cast(Optional[SystemType], self._getReq('system'))
        if r:
            self.system = self._decodeSystem(r)
            self.name = r['name']
        else:
            self.system = {}
            self.name = None
        return r

    def getAudiodata(self):
        audiodata = self._getReq('audio/volume')
        if audiodata:
            self.min_volume = int(audiodata['min'])
            self.max_volume = int(audiodata['max'])
            self.volume = audiodata['current'] / self.max_volume
            self.muted = audiodata['muted']
        else:
            self.min_volume = None
            self.max_volume = None
            self.volume = None
            self.muted = None
        return audiodata

    def getChannels(self):
        if self.api_version >= 5:
            self.channels = {}
            for channelListId in self.getChannelLists():
                r = cast(Optional[ChannelListType], self._getReq(
                    'channeldb/tv/channelLists/{}'.format(channelListId)
                ))
                if r:
                    for channel in r.get('Channel', []):
                        self.channels[str(channel['ccid'])] = channel
                return r
        else:
            r = cast(Optional[ChannelsType], self._getReq('channels'))
            if r:
                self.channels = r
            else:
                self.channels = {}
            return r

    def getChannelId(self):
        if self.api_version >= 5:
            r = cast(Optional[ActivitesTVType], self._getReq('activities/tv'))
            if r and r['channel']:
                # it could be empty if HDMI is set
                self.channel_id = str(r['channel']['ccid'])
            else:
                self.channel_id = None
        else:
            r = cast(Optional[ChannelsCurrentType], self._getReq('channels/current'))
            if not r:
                self.channel_id = None
                return

            if not self.channels.get(r['id']):
                pos = r['id'].find('_')
                if pos > 0:
                    self.channel_id = r['id'][pos+1:]
                    return
            self.channel_id = r['id']
        return r

    def getChannelName(self, ccid) -> Optional[str]:
        if not self.channels:
            return None
        return self.channels.get(ccid, dict()).get('name', None)

    def setChannel(self, ccid):
        if self.api_version >= 5:
            def setChannelBody(ccid):
                return {"channelList": {"id": "alltv"}, "channel": {"ccid": ccid}}
            if self._postReq('activities/tv', setChannelBody(ccid)):
                self.channel_id = ccid
        else:
            if self._postReq('channels/current', {'id': ccid}):
                self.channel_id = ccid

    def getChannelLists(self):
        if self.api_version >= 5:
            r = cast(ChannelDbTv, self._getReq('channeldb/tv'))
            if r:
                # could be alltv and allsat
                return [l['id'] for l in r.get('channelLists', [])]
            else:
                return []
        else:
            return []

    def getSources(self):
        if self.api_version < 5:
            r = self._getReq('sources')
            if r:
                self.sources = r
            else:
                self.sources = {}
            return r

    def getSourceId(self):
        if self.api_version < 5:
            r = self._getReq('sources/current')
            if r:
                self.source_id = r['id']
            else:
                self.source_id = None
            return r

    def getSourceName(self, srcid) -> Optional[str]:
        if not self.sources:
            return None
        if self.api_version < 5:
            return self.sources.get(srcid, dict()).get('name', None)
        return None

    def setSource(self, source_id):
        if self.api_version < 5:
            if self._postReq('sources/current', {'id': source_id}):
                self.source_id = source_id

    def getApplications(self):
        if self.api_version >= 5:
            r = cast(ApplicationsType, self._getReq('applications'))
            if r:
                self.applications = r
            else:
                self.applications = None
            return r

    def getApplication(self):
        if self.api_version >= 5:
            r = cast(ApplicationIntentType, self._getReq('activities/current'))
            if r:
                self.application = r
            else:
                self.application = None
            return r

    def getPowerState(self):
        if self.api_version >= 5:
            r = self._getReq('powerstate')
            if r:
                self.powerstate = cast(str, r["powerstate"])
            else:
                self.powerstate = None
        else:
            self.powerstate = None

    def setPowerState(self, state):
        if self.api_version >= 5:
            data = {
                "powerstate": state
            }
            if self._postReq('powerstate', data):
                self.powerstate = state
                return True
        return False

    def setApplication(self, intent: ApplicationIntentType):
        if self.api_version >= 5:
            data = {
                "intent": intent
            }
            if self._postReq('activities/launch', data):
                self.application = intent
                return True
        return False

    def setVolume(self, level, muted=False):
        data = {}
        if level is not None:
            if self.min_volume is None or self.max_volume is None:
                self.getAudiodata()
            assert(self.max_volume is not None)
            assert(self.min_volume is not None)

            try:
                targetlevel = int(level * self.max_volume)
            except ValueError:
                LOG.warning("Invalid audio level %s" % str(level))
                return False
            if targetlevel < self.min_volume or targetlevel > self.max_volume:
                LOG.warning("Level not in range (%i - %i)" % (self.min_volume, self.max_volume))
                return False
            data['current'] = targetlevel

        data['muted'] = muted

        if not self._postReq('audio/volume', data):
            return False

        self.volume = level
        self.muted = muted

    def sendKey(self, key):
        return self._postReq('input/key', {'key': key})

    def getAmbilightMode(self):
        data = self._getReq('ambilight/mode')
        return data["current"]

    def setAmbilightMode(self, mode):
        data = {
            "current": mode
        }
        return self._postReq('ambilight/mode', data)

    def getAmbilightTopology(self):
        return self._getReq('ambilight/topology')

    def getAmbilightMeasured(self):
        return self._getReq('ambilight/measured')

    def getAmbilightProcessed(self):
        return self._getReq('ambilight/processed')

    def getAmbilightCached(self):
        return self._getReq('ambilight/cached')

    def setAmbilightCached(self, data):
        return self._postReq('ambilight/cached', data)

    def openURL(self, url):
        if self.api_version >= 6:
            if (
                self.system and "browser" in (
                    self.system.get("featuring", {}).get("jsonfeatures", {}).get("activities", [])
                )
            ):
                self._postReq('activities/browser', {'url': url})
