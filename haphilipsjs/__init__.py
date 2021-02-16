from typing import Any, Dict, Optional, Tuple, TypeVar, Union, cast
import requests
from requests.auth import HTTPDigestAuth
import logging
import warnings
import urllib3
import json
from secrets import token_bytes, token_hex
from base64 import b64decode, b64encode

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hmac import HMAC

from .typing import ActivitesTVType, ActivitiesChannelType, ApplicationIntentType, ApplicationsType, ChannelDbTv, ChannelListType, ChannelType, ChannelsCurrentType, ChannelsType, ContextType, SystemType

LOG = logging.getLogger(__name__)
TIMEOUT = 5.0
DEFAULT_API_VERSION = 1

AUTH_SHARED_KEY = b64decode("ZmVay1EQVFOaZhwQ4Kv81ypLAZNczV9sG4KkseXWn1NEk6cXmPKO/MCa9sryslvLCFMnNe4Z4CPXzToowvhHvA==")
"""Key used for hmac signatures and decoding of cbc data."""

TV_PLAYBACK_INTENTS = [
    {
        'component': {
            'className': 'org.droidtv.playtv.PlayTvActivity',
            'packageName': 'org.droidtv.playtv'
        }
    }
]

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

def decode_xtv_json(text: str):
    if text == "" or text == "}":
        LOG.debug("Ignoring invalid json %s", text)
        return {}

    try:
        data = json.loads(text)
    except json.decoder.JSONDecodeError:
        LOG.debug("Invalid json received, trying adjusted version")
        text = text.replace("{,", "{")
        text = text.replace(",}", "}")
        while (p:= text.find(",,")) >= 0:
            text = text[:p] + text[p+1:]
        data = json.loads(text)

    return data


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
        self.sources = None
        self.source_id = None
        self.audio_volume = None
        self.channels: Optional[ChannelsType] = None
        self.channel: Optional[Union[ActivitesTVType, ChannelsCurrentType]] = None
        self.applications: Optional[ApplicationsType] = None
        self.application: Optional[ApplicationIntentType] = None
        self.context: Optional[ContextType] = None
        self.screenstate: Optional[str] = None
        self.ambilight_topology = None
        self.ambilight_mode = None
        self.ambilight_cached = None
        self.ambilight_measured = None
        self.ambilight_processed = None
        if auth_shared_key:
            self.auth_shared_key = auth_shared_key
        else:
            self.auth_shared_key = AUTH_SHARED_KEY

        if secured_transport:
            self.protocol = "https"
            self.port = 1926
        else:
            self.protocol = "http"
            self.port = 1925

        # for devices with notify support we must have two
        if self.api_version > 1:
            pool_maxsize=2
        else:
            pool_maxsize=1

        adapter = requests.sessions.HTTPAdapter(pool_connections=1, pool_maxsize=pool_maxsize, pool_block=True)
        self.session = requests.Session()
        self.session.verify=False
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers["Accept"] = "application/json"

        self.session.verify = verify
        if username:
            self.session.auth = HTTPDigestAuth(username, password)

    @property
    def quirk_playpause_spacebar(self):
        """Does this tv need workaround for playpause."""
        if self.system:
            return self.system.get("os_type", "").startswith("MSAF_")
        else:
            return None

    @property
    def pairing_type(self):
        if self.system:
            return self.system.get("featuring", {}).get("systemfeatures", {}).get("pairing_type")
        else:
            return None

    @property
    def secured_transport(self) -> Optional[bool]:
        if self.system:
            return self.system.get("featuring", {}).get("systemfeatures", {}).get("secured_transport") == "true"
        else:
            return None

    @property
    def notify_change_supported(self) -> Optional[str]:
        if self.system:
            return self.system.get("notifyChange", None)
        else:
            return None

    @property
    def api_version_detected(self) -> Optional[int]:
        if self.system:
            return self.system.get("api_version", {}).get("Major")
        else:
            return None

    @property
    def channel_active(self):
        if self.context and "level1" in self.context:
            return self.context["level1"] in ("WatchTv", "WatchSatellite")
        if self.context and "activity" in self.context:
            return self.context["activity"] in ("WatchTv", "WatchSatellite")
        if self.application:
            return self.application in TV_PLAYBACK_INTENTS
        if self.source_id in ("tv", "11", None):
            return self.channel_id is not None
        return False

    @property
    def min_volume(self):
        if self.audio_volume:
            return int(self.audio_volume['min'])
        else:
            return None

    @property
    def max_volume(self):
        if self.audio_volume:
            return int(self.audio_volume['max'])
        else:
            return None

    @property
    def volume(self):
        if self.audio_volume and int(self.audio_volume['max']):
            return self.audio_volume['current'] / int(self.audio_volume['max'])
        else:
            return None

    @property
    def muted(self):
        if self.audio_volume:
            return self.audio_volume['muted']
        else:
            return None

    @property
    def channel_id(self):
        if self.api_version >= 5:
            r = cast(Optional[ActivitesTVType], self.channel)
            if r and r['channel']:
                # it could be empty if HDMI is set
                return str(r['channel']['ccid'])
            else:
                return None
        else:
            r = cast(Optional[ChannelsCurrentType], self.channel)
            if not r:
                return None

            if not self.channels.get(r['id']):
                pos = r['id'].find('_')
                if pos > 0:
                    return r['id'][pos+1:]
            return r['id']

    def _url(self, path):
        return f'{self.protocol}://{self._host}:{self.port}/{self.api_version}/{path}'

    def _getReq(self, path) -> Optional[Dict]:

        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)
                with self.session.get(self._url(path), timeout=TIMEOUT) as resp:
                    if resp.status_code != 200:
                        return None
                    return decode_xtv_json(resp.text)
        except requests.exceptions.RequestException as err:
            raise ConnectionFailure(str(err)) from err

    def _getBinary(self, path: str) -> Tuple[Optional[bytes], Optional[str]]:

        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)
                with self.session.get(self._url(path), timeout=TIMEOUT) as resp:
                    if resp.status_code != 200:
                        return None, None
                    return resp.content, resp.headers["Content-Type"]
        except requests.exceptions.RequestException as err:
            raise ConnectionFailure(str(err)) from err

    def _postReq(self, path: str, data: Dict, timeout=TIMEOUT) -> Optional[Dict]:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)

                with self.session.post(self._url(path), json=data, timeout=timeout) as resp:
                    if resp.status_code == 200:
                        LOG.debug("Post succeded: %s -> %s", data, resp.text)
                        if resp.headers.get('content-type', "").startswith("application/json"):
                            return decode_xtv_json(resp.text)
                        else:
                            return {}
                    else:
                        LOG.warning("Post failed: %s -> %s", data, resp.text)
                        return None
        except requests.exceptions.ReadTimeout:
            return None
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

    def setTransport(self, secured_transport: Optional[bool] = None, api_version: Optional[int] = None):
        if secured_transport == True and self.protocol != "https":
            LOG.info("Switching to secured transport")
            self.protocol = "https"
            self.port = 1926
        elif secured_transport == False and self.protocol != "http":
            LOG.info("Switching to unsecured transport")
            self.protocol = "http"
            self.port = 1925

        if api_version and api_version != self.api_version:
            LOG.info("Switching to api_version %d", api_version)
            self.api_version = api_version


    def update(self):
        try:
            if not self.on:
                self.getSystem()
                self.setTransport(self.secured_transport)
                self.getSources()
                self.getChannels()
                self.getApplications()

            self.getPowerState()
            self.getAudiodata()
            self.getSourceId()
            self.getChannelId()
            self.getApplication()
            self.getContext()
            self.getScreenState()
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
        r = self._getReq('audio/volume')
        if r:
            self.audio_volume = r
        else:
            self.audio_volume = r
        return r

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
        else:
            r = cast(Optional[ChannelsCurrentType], self._getReq('channels/current'))

        self.channel = r
        return r

    def getChannelName(self, ccid) -> Optional[str]:
        if not self.channels:
            return None
        return self.channels.get(ccid, dict()).get('name', None)

    def getChannelLogo(self, ccid, channel_list="all") -> Tuple[Optional[bytes], Optional[str]]:
        if self.api_version >= 5:
            data, content_type = self._getBinary(f"channeldb/tv/channelLists/{channel_list}/{ccid}/logo")
        else:
            data, content_type = self._getBinary(f"channels/{ccid}/logo.png")
        return data, content_type

    def getContext(self) -> Optional[ContextType]:
        if self.api_version >= 5:
            r = cast(Optional[ContextType], self._getReq(f"context"))
            self.context = r
            return r

    def setChannel(self, ccid):
        channel: Union[ActivitesTVType, ChannelsCurrentType]
        if self.api_version >= 5:
            channel = {"channelList": {"id": "alltv"}, "channel": {"ccid": ccid}}
            if self._postReq('activities/tv', cast(Dict, channel)) is not None:
                self.channel = channel
        else:
            channel = {'id': ccid}
            if self._postReq('channels/current', cast(Dict, channel)) is not None:
                self.channel = channel

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
            if self._postReq('sources/current', {'id': source_id}) is not None:
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

    def getApplicationIcon(self, id) -> Tuple[Optional[bytes], Optional[str]]:
        if self.api_version >= 5:
            data, content_type = self._getBinary(f"applications/{id}/icon")
            return data, content_type
        else:
            return None, None

    def getPowerState(self):
        if self.api_version >= 5:
            r = self._getReq('powerstate')
            if r:
                self.powerstate = cast(str, r["powerstate"])
            else:
                self.powerstate = None
            return r
        else:
            self.powerstate = None

    def setPowerState(self, state):
        if self.api_version >= 5:
            data = {
                "powerstate": state
            }
            if self._postReq('powerstate', data) is not None:
                self.powerstate = state
                return True
        return False

    def getScreenState(self):
        if self.api_version >= 5:
            r = self._getReq('screenstate')
            if r:
                self.screenstate = cast(str, r["screenstate"])
            else:
                self.screenstate = None
            return r
        else:
            self.screenstate = None

    def setScreenState(self, state):
        if self.api_version >= 5:
            data = {
                "screenstate": state
            }
            if self._postReq('screenstate', data) is not None:
                self.screenstate = state
                return True
        return False

    def setApplication(self, intent: ApplicationIntentType):
        if self.api_version >= 5:
            data = {
                "intent": intent
            }
            if self._postReq('activities/launch', data) is not None:
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

        if self._postReq('audio/volume', data) is None:
            return False

        self.audio_volume.update(data)

    def sendKey(self, key):
        res = self._postReq('input/key', {'key': key}) is not None
        if res:
            if key == "Mute":
                if self.audio_volume:
                    self.audio_volume["muted"] = not self.audio_volume["muted"]
            elif key == "VolumeUp":
                if self.audio_volume and self.audio_volume["current"] < self.audio_volume["max"]:
                    self.audio_volume["current"] += 1
            elif key == "VolumeDown":
                if self.audio_volume and self.audio_volume["current"] > self.audio_volume["min"]:
                    self.audio_volume["current"] -= 1

    def sendUnicode(self, key: str):
        return self._postReq('input/key', {'unicode': key}) is not None

    def getAmbilightMode(self):
        data = self._getReq('ambilight/mode')
        if data:
            self.ambilight_mode = data["current"]
            return data["current"]
        else:
            self.ambilight_mode = None

    def setAmbilightMode(self, mode):
        data = {
            "current": mode
        }
        if self._postReq('ambilight/mode', data) is None:
            return False
        self.ambilight_mode = mode
        return True

    def getAmbilightTopology(self):
        r = self._getReq('ambilight/topology')
        if r:
            self.ambilight_topology = r
        else:
            self.ambilight_topology = None            

    def getAmbilightMeasured(self):
        r = self._getReq('ambilight/measured')
        if r:
            self.ambilight_measured = r
        else:
            self.ambilight_measured = None

    def getAmbilightProcessed(self):
        r = self._getReq('ambilight/processed')
        if r:
            self.ambilight_processed = r
        else:
            self.ambilight_processed = None

    def getAmbilightCached(self):
        r = self._getReq('ambilight/cached')
        if r:
            self.ambilight_cached = r
        else:
            self.ambilight_cached = None

    def setAmbilightCached(self, data):
        if self._postReq('ambilight/cached', data) is None:
            return False
        self.ambilight_cached = data
        return True

    def openURL(self, url):
        if self.api_version >= 6:
            if (
                self.system and "browser" in (
                    self.system.get("featuring", {}).get("jsonfeatures", {}).get("activities", [])
                )
            ):
                self._postReq('activities/browser', {'url': url})

    def notifyChange(self, timeout = 30):
        """Start a http connection waiting for changes."""
        if not self.notify_change_supported:
            return None

        data = {
            "notification": {
                "activities/tv": self.channel,
                "activities/current": self.application,
                "powerstate": {"powerstate": self.powerstate},
                "audio/volume": self.audio_volume,
                "context": self.context,
                "screenstate": {"screenstate": self.screenstate},
            }
        }
        try:
            result = self._postReq('notifychange', data=data, timeout=timeout)
        except ConnectionFailure as err:
            LOG.debug("Exception: %s", str(err))
            self.on = False
            result = None
        if result:
            if "activities/tv" in result:
                self.channel = result["activities/tv"]

            if "activities/current" in result:
                self.application = result["activities/current"]

            if "powerstate" in result:
                self.powerstate = result["powerstate"]["powerstate"]

            if "audio/volume" in result:
                self.audio_volume = result["audio/volume"]

            if "context" in result:
                self.context = result["context"]

            if "screenstate" in result:
                self.screenstate = result["screenstate"]["screenstate"]
            return True
        else:
            return False
