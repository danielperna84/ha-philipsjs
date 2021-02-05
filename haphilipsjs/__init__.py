from typing import Any, Dict, Optional, TypeVar, cast
import requests
from requests.auth import HTTPDigestAuth
import logging
import warnings
import urllib3
from secrets import token_bytes, token_hex
from base64 import b64encode

import hashlib
import hmac

from .typing import ActivitesTVType, ApplicationIntentType, ChannelDbTv, ChannelListType, ChannelsCurrentType, SystemType

LOG = logging.getLogger(__name__)
TIMEOUT = 5.0
DEFAULT_API_VERSION = 1


def gen_pair_secret():
    return token_bytes(64)

class ConnectionFailure(Exception):
    pass

class PairingFailure(Exception):
    pass

T = TypeVar('T') 

class PhilipsTV(object):

    def __init__(self, host=None, api_version=DEFAULT_API_VERSION, protocol="http", port=1925, username=None, password=None, verify=False):
        self._host = host
        self._connfail = 0
        self.api_version = int(api_version)
        self.on = False
        self.name = None
        self.system: Optional[SystemType] = None
        self.min_volume = None
        self.max_volume = None
        self.volume = None
        self.muted = None
        self.sources = None
        self.source_id = None
        self.channels = None
        self.channel_id = None
        self.protocol = protocol
        self.port = port

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
                        return True
                    else:
                        return False
        except requests.exceptions.RequestException as err:
            raise ConnectionFailure(str(err)) from err

    def pairRequest(self, app_id: str, app_name: str, device_name: str, device_os: str, type: str):
        """Start up a pairing request."""
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
                try:
                    data_response = resp.json()
                    LOG.debug("pair/request response: %s", data_response)
                    if data_response.get("error_id") != "SUCCESS":
                        raise PairingFailure(f"Failed to start pairing: {data_response}")
                except ValueError as exc:
                    raise PairingFailure(f"Failed to start pairing no valid json returned") from exc

        state["timestamp"] = data_response["timestamp"]
        state["auth_key"] = data_response["auth_key"]

        return state

    def pairGrant(self, state: Dict[str, Any], pin: str, key: bytes):
        """Finish a pairing sequence"""

        auth_handler = HTTPDigestAuth(
            state["device"]["id"],
            state["auth_key"]
        )

        signature = b64encode(hmac.new(
            key=key,
            msg=bytes(f"{state['timestamp']}{pin}", "utf-8"),
            digestmod=hashlib.sha256,
        ).digest()).decode("utf-8")

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
                data_response = resp.json()
                LOG.debug("pair/grant response: %s", data_response)

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

            self.getAudiodata()
            self.getSourceId()
            self.getChannelId()
            self.on = True
            return True
        except ConnectionFailure as err:
            LOG.debug("Exception: %s", str(err))
            self.on = False
            return False

    def getSystem(self):
        r = cast(Optional[SystemType], self._getReq('system'))
        if r:
            self.system = r
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
                r = cast(ChannelListType, self._getReq(
                    'channeldb/tv/channelLists/{}'.format(channelListId)
                ))
                if r:
                    for channel in r.get('Channel', []):
                        self.channels[channel['ccid']] = channel
                return r
        else:
            r = self._getReq('channels')
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
                self.channel_id = r['channel']['ccid']
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

    def setSource(self, source_id):
        if self.api_version < 5:
            if self._postReq('sources/current', {'id': source_id}):
                self.source_id = source_id

    def getApplications(self):
        if self.api_version >= 5:
            return self._getReq('applications')

    def getApplicationId(self):
        if self.api_version >= 5:
            return cast(ApplicationIntentType, self._getReq('activities/current'))

    def setVolume(self, level, muted=False):
        data = {}
        if level is not None:
            if self.min_volume is None or self.max_volume is None:
                self.getAudiodata()
            assert(self.max_volume)
            assert(self.min_volume)

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
