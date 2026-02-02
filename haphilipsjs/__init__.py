from typing import Any, Dict, List, Optional, Tuple, TypeVar, Union, cast, overload, Iterable, TypeVar
import httpx
import logging
import json
import itertools
from urllib.parse import quote
from secrets import token_bytes, token_hex
from base64 import b64decode, b64encode
from functools import wraps


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.hmac import HMAC

from .typing import (
    ActivitesTVType,
    AmbilightCurrentConfiguration,
    AmbilightLayersType,
    AmbilightSupportedStyleType,
    AmbilightSupportedStylesType,
    ApplicationIntentType,
    ApplicationsType,
    ChannelDbTv,
    ChannelListType,
    ChannelsCurrentType,
    ChannelsType,
    ChannelType,
    ContextType,
    FavoriteListType,
    RecordingsListed,
    MenuItemsSettingsCurrent,
    MenuItemsSettingsCurrentPost,
    MenuItemsSettingsCurrentValueValue,
    MenuItemsSettingsEntry,
    MenuItemsSettingsNode,
    MenuItemsSettingsStructure,
    MenuItemsSettingsUpdate,
    MenuItemsSettingsUpdateValueData,
    Strings,
    StringsRequest,
    SystemType,
    ApplicationType,
)
from .auth import CachedDigestAuth

LOG = logging.getLogger(__name__)
TIMEOUT = 20.0
TIMEOUT_CONNECT = 5.0
TIMEOUT_NOTIFYREAD = 130
DEFAULT_API_VERSION = 1

AUTH_SHARED_KEY = b64decode(
    "ZmVay1EQVFOaZhwQ4Kv81ypLAZNczV9sG4KkseXWn1NEk6cXmPKO/MCa9sryslvLCFMnNe4Z4CPXzToowvhHvA=="
)
"""Key used for hmac signatures and decoding of cbc data."""

TV_PLAYBACK_INTENTS = [
    {
        "component": {
            "className": "org.droidtv.playtv.PlayTvActivity",
            "packageName": "org.droidtv.playtv",
        }
    }
]

HTTP_PORT = 1925
HTTPS_PORT = 1926
MAXIMUM_ITEMS_IN_REQUEST = 50
IGNORED_JSON_RESPONSES = {"", "Context Service not started", "}", "<html><head><title>Ok</title></head><body>Ok</body></html>", }

def hmac_signature(key: bytes, timestamp: str, data: str):
    """Calculate a timestamped signature."""
    hmac = HMAC(key, SHA1())
    hmac.update(timestamp.encode("utf-8"))
    hmac.update(data.encode("utf-8"))
    return b64encode(hmac.finalize()).decode("utf-8")


def cbc_decode(key: bytes, data: str):
    """Decoded encrypted fields based on shared key."""
    if data == "":
        return ""
    raw = b64decode(data)
    assert len(raw) >= 16, f"Lenght of data too short: '{data}'"
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
    try:
        data = json.loads(text)
    except json.decoder.JSONDecodeError:
        LOG.debug("Invalid json received, trying adjusted version")
        text = text.replace('"channelList": { "id": "version", "" }', '"channelList": { "id": "all", "version": "" }')
        text = text.replace("{,", "{")
        text = text.replace(",}", "}")
        while (p := text.find(",,")) >= 0:
            text = text[:p] + text[p + 1 :]

        try:
            data = json.loads(text)
        except json.decoder.JSONDecodeError as exception:
            raise NoneJsonData(text) from exception

    return data


def decode_xtv_response(response: httpx.Response):
    try:
        text = response.text
    except UnicodeDecodeError:
        LOG.warning("Unable to decode unicode on endpoint, ignoring", exc_info=True)
        return {}

    if text in IGNORED_JSON_RESPONSES:
        LOG.debug("Ignoring invalid json %s", text)
        return {}

    if not response.headers.get("content-type", "").startswith("application/json"):
        if text:
            LOG.warning("Non json data: %s", text)
        return {}

    return decode_xtv_json(text)


_T = TypeVar("_T")

def chunked_iterator(size: int, iterable: Iterable[_T]) -> Iterable[Iterable[_T]]:
    """Create a chain of iterators that each will give a chunk of the original."""
    step = iter(iterable)
    while True:
        chunk_it = itertools.islice(step, size)
        try:
            first_el = next(chunk_it)
        except StopIteration:
            return
        yield itertools.chain((first_el,), chunk_it)


PASSTHROUGH_URI = "content://android.media.tv/passthrough"


def passthrough_uri(data):
    return f"{PASSTHROUGH_URI}/{quote(data, safe='')}"


CHANNEL_URI = "content://android.media.tv/channel"


def channel_uri(channel):
    uri = CHANNEL_URI
    if channel is not None:
        uri += f"/{channel}"
    return uri


class GeneralFailure(Exception):
    """Base class for component failures."""


class ConnectionFailure(GeneralFailure):
    """Failed to connect to tv it's likely turned off."""


class ProtocolFailure(GeneralFailure):
    """Wrapper to contain erros that are the server closing a connection before response."""


class AutenticationFailure(GeneralFailure):
    """Wrapper to contain failures due to authentication."""


class PairingFailure(GeneralFailure):
    def __init__(self, data):
        super().__init__(f"Failed to start pairing: {data}")
        self.data = data


class NoneJsonData(GeneralFailure):
    """API Returned non json data when json was expected."""
    def __init__(self, data):
        super().__init__(f"Non json data received: {data}")
        self.data = data


T = TypeVar("T")


def handle_httpx_exceptions(f):
    """Wrap up httpx exceptions in our wanted variants."""
    @wraps(f)
    async def wrapper(*args, **kwds):
        try:
            try:
                return await f(*args, **kwds)
            except httpx.RemoteProtocolError as err:
                LOG.debug("%r. We retry once, could be a reused session that was closed", err)
                return await f(*args, **kwds)

        except (httpx.ConnectTimeout, httpx.ConnectError) as err:
            raise ConnectionFailure(err) from err
        except (httpx.ProtocolError, httpx.ReadError) as err:
            raise ProtocolFailure(err) from err
        except httpx.HTTPError as err:
            raise GeneralFailure(err) from err

    return wrapper


class PhilipsTV(object):

    channels: ChannelsType
    """All available channels, with ccid as key."""

    def __init__(
        self,
        host=None,
        api_version=DEFAULT_API_VERSION,
        secured_transport=None,
        username=None,
        password=None,
        verify=False,
        auth_shared_key=None,
        system = None,
        limits = None,
    ):
        self._host = host
        self._connfail = 0
        self.api_version = int(api_version)
        self.on = False
        self.name: Optional[str] = None
        self.system: Optional[SystemType] = system
        self.strings: dict[str, str] = {}
        self.sources = {}
        self.source_id = None
        self.audio_volume = None
        self.channels = {}
        self.channel: Optional[Union[ActivitesTVType, ChannelsCurrentType]] = None
        self.channel_lists: Dict[str, ChannelListType] = {}
        self.favorite_lists: Dict[str, FavoriteListType] = {}
        self.applications: Dict[str, ApplicationType] = {}
        self.application: Optional[ApplicationIntentType] = None
        self.context: Optional[ContextType] = None
        self.screenstate: Optional[str] = None
        self.settings: Optional[MenuItemsSettingsStructure] = None
        self.settings_version = 0
        self.ambilight_topology = None
        self.ambilight_mode_set = None
        self.ambilight_mode_raw: Optional[str] = None
        self.ambilight_cached: Optional[AmbilightLayersType] = None
        self.ambilight_measured: Optional[AmbilightLayersType] = None
        self.ambilight_processed: Optional[AmbilightLayersType] = None
        self.ambilight_power_raw: Optional[Dict] = None
        self.ambilight_styles: Dict[str, AmbilightSupportedStyleType] = {}
        self.ambilight_current_configuration: Optional[
            AmbilightCurrentConfiguration
        ] = None
        self.recordings_list: Optional[RecordingsListed] = None
        self.huelamp_power: Optional[str] = None
        self.powerstate = None
        if auth_shared_key:
            self.auth_shared_key = auth_shared_key
        else:
            self.auth_shared_key = AUTH_SHARED_KEY

        if secured_transport or self.secured_transport:
            self.protocol = "https"
        else:
            self.protocol = "http"

        timeout = httpx.Timeout(timeout=TIMEOUT, connect=TIMEOUT_CONNECT)
        if limits is None:
            limits = httpx.Limits(max_keepalive_connections=3, max_connections=3)
        self.session = httpx.AsyncClient(limits=limits, timeout=timeout, verify=False)
        self.session.headers["Accept"] = "application/json"

        if username and password:
            self.session.auth = CachedDigestAuth(username, password)

    @property
    def quirk_playpause_spacebar(self):
        """Does this tv need workaround for playpause."""
        if self.system:
            return self.system.get("os_type", "").startswith("MSAF_")
        else:
            return False

    @property
    def quirk_ambilight_styles_menuitems(self):
        if self.system:
            return self.system.get("os_type", "").startswith("MSAF_")
        else:
            return False

    @property
    def os_type(self):
        if self.system is None:
            return None

        # android system have in direclty in root
        os_type = self.system.get("os_type")
        if os_type:
            return os_type

        # saphi stores in in features
        os_type = (
            self.system.get("featuring", {}).get("systemfeatures", {}).get("os_type")
        )
        if os_type:
            return os_type

        return None

    @property
    def quirk_ambilight_mode_ignored(self):
        """Return if this tv need workaround for ambilight bugs.

        XTV app have bugs with their mode management for ambilight. It will
        forgot to actuate the command to set mode back to internal. But will actually
        do that if you give it an invalid mode.

        It will also not report a correct ambilight mode after being
        changed by call. So we need to remember last set mode.

        Versions known affected:
            - Android - 9.0.0
            - Saphi - 4.6.0.2

        Version known good
            - Legacy - QF1EU-0.150.102.0
        """

        os_type = self.os_type
        if os_type:
            if os_type.startswith("MSAF_"):
                return True

            if os_type == "Linux":
                return True

        return False

    @property
    def pairing_type(self):
        if self.system:
            return (
                self.system.get("featuring", {})
                .get("systemfeatures", {})
                .get("pairing_type")
            )
        else:
            return None

    @property
    def secured_transport(self) -> Optional[bool]:
        if self.system:
            return (
                self.system.get("featuring", {})
                .get("systemfeatures", {})
                .get("secured_transport")
                in ("true", True)
            )
        else:
            return None

    @property
    def notify_change_supported(self) -> Optional[str]:
        if self.system:
            return self.system.get("notifyChange", None)
        else:
            return None

    @overload
    def json_feature_supported(self, type: str) -> Optional[List[str]]:
        ...

    @overload
    def json_feature_supported(self, type: str, value: str) -> Optional[bool]:
        ...

    def json_feature_supported(self, type: str, value: Optional[str] = None):
        if self.system:
            features = cast(
                List[str],
                self.system.get("featuring", {}).get("jsonfeatures", {}).get(type, []),
            )
            if value:
                return value in features
            else:
                return features
        else:
            return None

    @property
    def api_version_detected(self) -> Optional[int]:
        if self.system:
            return cast(Optional[int], self.system.get("api_version", {}).get("Major"))
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
    def application_id(self):
        if self.application and "component" in self.application:
            component = self.application["component"]
            app_id = f"{component.get('className', 'None')}-{component.get('packageName', 'None')}"
            if app_id in self.applications:
                return app_id
            else:
                return None
        else:
            return None

    @property
    def min_volume(self):
        if self.audio_volume:
            return int(self.audio_volume["min"])
        else:
            return None

    @property
    def max_volume(self):
        if self.audio_volume:
            return int(self.audio_volume["max"])
        else:
            return None

    @property
    def volume(self):
        if self.audio_volume and int(self.audio_volume["max"]):
            return self.audio_volume["current"] / int(self.audio_volume["max"])
        else:
            return None

    @property
    def muted(self):
        if self.audio_volume:
            return self.audio_volume["muted"]
        else:
            return None

    @property
    def channel_id(self):
        if self.api_version >= 5:
            r = cast(Optional[ActivitesTVType], self.channel)
            if not r:
                return None

            ccid = r.get("channel", {}).get("ccid")
            # it could be empty if HDMI is set
            if not ccid:
                return None
            return str(ccid)
        else:
            r = cast(Optional[ChannelsCurrentType], self.channel)
            if not r:
                return None

            if not self.channels.get(r["id"]):
                pos = r["id"].find("_")
                if pos > 0:
                    return r["id"][pos + 1 :]
            return r["id"]

    @property
    def channel_list_id(self) -> str:
        if self.api_version >= 5:
            if not self.channel:
                return "all"
            r = cast(ActivitesTVType, self.channel)
            channel_list = r.get("channelList")
            if not channel_list:
                return "all"
            return channel_list.get("id", "all")

        return "all"

    @property
    def channels_current(self) -> List[ChannelType]:
        """All channels in the current favorite list."""
        if self.api_version >= 5:
            favorite_list = self.favorite_lists.get(self.channel_list_id)
            if not favorite_list:
                return list(self.channels.values())

            return [
                {
                    **channel,
                    "preset": favorite.get("preset", "")
                }
                for favorite in favorite_list.get("channels", [])
                if (channel := self.channels.get(str(favorite.get("ccid"))))
            ]
        else:
            return [
                {
                    **channel,
                    "ccid": key
                }
                for key, channel in self.channels.items()
            ]

    @property
    def ambilight_modes(self):
        modes = ["internal", "manual", "expert"]

        if self.api_version >= 6:
            features = self.json_feature_supported("ambilight")
            if features:
                if "LoungeLight" in features:
                    modes.append("lounge")
                return modes
            else:
                return []
        else:
            return modes

    @property
    def ambilight_mode(self) -> Optional[str]:
        if self.quirk_ambilight_mode_ignored:
            if self.ambilight_mode_set:
                return self.ambilight_mode_set
        return self.ambilight_mode_raw

    @property
    def ambilight_power(self) -> Optional[str]:

        if self.api_version >= 5:
            if self.ambilight_power_raw is None:
                return None
            return self.ambilight_power_raw.get("power")

        if self.api_version == 1:
            if self.ambilight_cached is None:
                return None

            if self.ambilight_mode == "manual":
                if any(
                    color != 0
                    for layer in self.ambilight_cached.values()
                    for side in layer.values()
                    for pixel in side.values()
                    for color in pixel.values()
                ):
                    return "On"
                else:
                    return "Off"

            else:
                return "On"

        return None

    async def aclose(self) -> None:
        await self.session.aclose()

    def _url(self, path, protocol = None):
        if protocol is None:
            protocol = self.protocol

        if protocol == "https":
            port = HTTPS_PORT
        else:
            port = HTTP_PORT

        return f"{protocol}://{self._host}:{port}/{self.api_version}/{path}"

    @handle_httpx_exceptions
    async def getReq(self, path, protocol = None) -> Optional[Dict]:
        resp = await self.session.get(self._url(path, protocol = protocol))

        if resp.status_code == 401:
            raise AutenticationFailure("Authenticaion failed to device")

        if resp.status_code != 200:
            LOG.debug("Get failed: %s -> %d %s", path, resp.status_code, resp.text)
            return None

        LOG.debug("Get succeded: %s -> %s", path, resp.text)
        return decode_xtv_response(resp)
  
    @handle_httpx_exceptions
    async def _getBinary(self, path: str) -> Tuple[Optional[bytes], Optional[str]]:

        resp = await self.session.get(self._url(path))
        if resp.status_code == 401:
            raise AutenticationFailure("Authenticaion failed to device")

        if resp.status_code != 200:
            return None, None
        return resp.content, resp.headers.get("content-type")

    @handle_httpx_exceptions
    async def postReq(self, path: str, data: Any, timeout=None, protocol=None) -> Optional[Dict]:
        try:
            resp = await self.session.post(self._url(path, protocol), json=data, timeout=timeout)
            if resp.status_code == 401:
                raise AutenticationFailure("Authenticaion failed to device")

            if resp.status_code == 200:
                LOG.debug("Post succeded: %s -> %s", data, resp.text)
                return decode_xtv_response(resp)

            LOG.warning("Post failed: %s -> %s", data, resp.text)
            return None
        except httpx.ReadTimeout:
            LOG.debug("Read time out on postReq", exc_info=True)
            return None

    async def pairRequest(
        self,
        app_id: str,
        app_name: str,
        device_name: str,
        device_os: str,
        type: str,
        device_id: Optional[str] = None,
    ):
        """Start up a pairing request."""
        if device_id is None:
            device_id = token_hex(16)

        device = {
            "device_name": device_name,
            "device_os": device_os,
            "type": type,
            "id": device_id,
            "app_id": app_id,
            "app_name": app_name,
        }

        state = {"device": device}

        data = {
            "access": {
                "scope": ["read", "write", "control"]
            },
            "device": device
        }

        if self.system:
            featuring = self.system.get("featuring", None)
            if featuring:
                data["access"]["featuring"] = featuring


        LOG.debug("pair/request request: %s", data)
        resp = await self.session.post(self._url("pair/request"), json=data, auth=None)
        if not resp.headers["content-type"].startswith("application/json"):
            raise NoneJsonData(resp.text)
        data_response = resp.json()

        LOG.debug("pair/request response: %s", data_response)
        if data_response.get("error_id") != "SUCCESS":
            raise PairingFailure(data_response)

        state["timestamp"] = data_response["timestamp"]
        state["auth_key"] = data_response["auth_key"]

        return state

    async def pairGrant(self, state: Dict[str, Any], pin: str):
        """Finish a pairing sequence"""
        auth_handler = httpx.DigestAuth(state["device"]["id"], state["auth_key"])

        signature = hmac_signature(self.auth_shared_key, str(state["timestamp"]), pin)

        auth = {
            "auth_appId": "1",
            "auth_timestamp": state["timestamp"],
            "auth_signature": signature,
            "pin": pin,
        }

        data = {"auth": auth, "device": state["device"]}

        LOG.debug("pair/grant request: %s", data)
        resp = await self.session.post(
            self._url("pair/grant"), json=data, auth=auth_handler
        )
        if not resp.headers["content-type"].startswith("application/json"):
            raise NoneJsonData(resp.text)
        data_response = resp.json()
        LOG.debug("pair/grant response: %s", data_response)

        if data_response.get("error_id") != "SUCCESS":
            raise PairingFailure(data_response)

        self.session.auth = auth_handler
        return state["device"]["id"], state["auth_key"]

    async def setTransport(
        self,
        secured_transport: Optional[bool] = None,
        api_version: Optional[int] = None,
    ):
        if secured_transport == True and self.protocol != "https":
            LOG.info("Switching to secured transport")
            self.protocol = "https"
        elif secured_transport == False and self.protocol != "http":
            LOG.info("Switching to unsecured transport")
            self.protocol = "http"

        if api_version and api_version != self.api_version:
            LOG.info("Switching to api_version %d", api_version)
            self.api_version = api_version

    async def update(self):
        try:
            if not self.on:
                await self.getSystem()
                await self.setTransport(self.secured_transport)
                await self.getSources()
                await self.getChannelLists()
                await self.getChannels()
                await self.getApplications()
                await self.getAmbilightSupportedStyles()
                await self.getAmbilightCached()
                await self.getMenuItemsSettingsStructure()

            await self.getPowerState()
            await self.getAudiodata()
            await self.getSourceId()
            await self.getChannelId()
            await self.getApplication()
            await self.getContext()
            await self.getScreenState()
            await self.getAmbilightMode()
            await self.getAmbilightPower()
            await self.getAmbilightCurrentConfiguration()
            await self.getHueLampPower()
            await self.getRecordings()
            self.on = True
            return True
        except ConnectionFailure as err:
            LOG.debug("TV not available: %s", repr(err))
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

    async def getSystem(self):
        # Newest TV software requires https for system-info. Therefore we will try both protocols.
        protocols = ["http", "https"]

        if protocols[0] != self.protocol:
            protocols = reversed(protocols)
        
        for prot in protocols:
            r = cast(Optional[SystemType], await self.getReq("system", protocol=prot))
            if r:
                self.system = self._decodeSystem(r)
                self.name = r.get("name")
                return r
            else:
                self.system = {}
                self.name = None
        return r

    async def getAudiodata(self):
        r = await self.getReq("audio/volume")
        if r:
            self.audio_volume = r
        else:
            self.audio_volume = r
        return r

    async def getChannels(self):
        if self.api_version >= 5:
            self.channels = {}
            for channel_list in self.channel_lists.values():
                for channel in channel_list.get("Channel", []):
                    self.channels[str(channel.get("ccid"))] = channel
            return self.channels
        else:
            r = cast(Optional[ChannelsType], await self.getReq("channels"))
            if r:
                self.channels = r
            else:
                self.channels = {}
            return r

    async def getChannelId(self):
        if not self.channels:
            self.channel = None
            return None

        if self.api_version >= 5:
            r = cast(Optional[ActivitesTVType], await self.getReq("activities/tv"))
        else:
            r = cast(
                Optional[ChannelsCurrentType], await self.getReq("channels/current")
            )

        self.channel = r
        return r

    async def getChannelName(self, ccid) -> Optional[str]:
        if not self.channels:
            return None
        return self.channels.get(ccid, dict()).get("name", None)

    async def getChannelLogo(
        self, ccid, channel_list="all"
    ) -> Tuple[Optional[bytes], Optional[str]]:
        if self.api_version >= 5:
            data, content_type = await self._getBinary(
                f"channeldb/tv/channelLists/{channel_list}/{ccid}/logo"
            )
        else:
            data, content_type = await self._getBinary(f"channels/{ccid}/logo.png")
        return data, content_type

    async def getContext(self) -> Optional[ContextType]:
        r = cast(Optional[ContextType], await self.getReq(f"context"))
        self.context = r
        return r

    async def setChannel(self, ccid: Union[str, int], list_id: Optional[str] = None):
        channel: Union[ActivitesTVType, ChannelsCurrentType]
        if self.api_version >= 5:
            channel = {"channelList": {"id": list_id or "all"}, "channel": {"ccid": int(ccid)}}
            if await self.postReq("activities/tv", cast(Dict, channel)) is not None:
                self.channel = channel
                return True
        else:
            channel = {"id": str(ccid)}
            if await self.postReq("channels/current", cast(Dict, channel)) is not None:
                self.channel = channel
                return True
        return False

    async def getChannelLists(self):
        if self.api_version >= 5:
            r = cast(ChannelDbTv, await self.getReq("channeldb/tv"))
            if r:
                channel_lists = {}
                favorite_lists = {}

                for data in r.get("channelLists", []):
                    list_id = data["id"]
                    channel_list = cast(
                        Optional[ChannelListType],
                        await self.getReq(f"channeldb/tv/channelLists/{list_id}"),
                    )
                    if channel_list:
                        channel_lists[list_id] = channel_list


                for data in r.get("favoriteLists", []):
                    list_id = data["id"]
                    favorite_list = cast(
                        Optional[FavoriteListType],
                        await self.getReq(f"channeldb/tv/favoriteLists/{list_id}"),
                    )
                    if favorite_list:
                        favorite_lists[list_id] = favorite_list

                self.channel_lists = channel_lists
                self.favorite_lists = favorite_lists
            else:
                self.channel_lists = {}
                self.favorite_lists = {}

            return r

    async def getFavoriteList(self, list_id: str):
        if self.api_version >= 5:
            r = cast(
                Optional[FavoriteListType],
                await self.getReq(f"channeldb/tv/favoriteLists/{list_id}"),
            )
            if r and "channels" in r:
                return r["channels"]
            else:
                return None

    async def getChannelList(self, list_id: str):
        if self.api_version >= 5:
            r = cast(
                Optional[ChannelListType],
                await self.getReq(f"channeldb/tv/channelLists/{list_id}"),
            )
            if r and "Channel" in r:
                return r["Channel"]
            else:
                return None

    async def getSources(self):
        if self.json_feature_supported("activities", "intent"):
            self.sources = {
                channel_uri(None): {"name": "Watch TV"},
                passthrough_uri("com.mediatek.tvinput/.hdmi.HDMIInputService/HW5"): {
                    "name": "HDMI 1"
                },
                passthrough_uri("com.mediatek.tvinput/.hdmi.HDMIInputService/HW6"): {
                    "name": "HDMI 2"
                },
                passthrough_uri("com.mediatek.tvinput/.hdmi.HDMIInputService/HW7"): {
                    "name": "HDMI 3"
                },
                passthrough_uri("com.mediatek.tvinput/.hdmi.HDMIInputService/HW8"): {
                    "name": "HDMI 4"
                },
            }
            return self.sources

        if self.api_version == 1:
            r = await self.getReq("sources")
            if r:
                self.sources = r
            else:
                self.sources = {}
            return r

    async def getSourceId(self):
        if self.api_version < 5:
            r = await self.getReq("sources/current")
            if r:
                self.source_id = r["id"]
            else:
                self.source_id = None
            return r

    async def getSourceName(self, srcid) -> Optional[str]:
        if not self.sources:
            return None
        return self.sources.get(srcid, dict()).get("name", None)

    async def setSource(self, source_id):
        if self.api_version == 1:
            r = await self.postReq("sources/current", {"id": source_id})
            if r is not None:
                return True
            return False

        if self.json_feature_supported("activities", "intent"):
            if source_id == CHANNEL_URI and self.channel_id:
                source_id = channel_uri(self.channel_id)

            intent: ApplicationIntentType = {
                "extras": {"uri": source_id},
                "action": "org.droidtv.playtv.SELECTURI",
                "component": {
                    "packageName": "org.droidtv.playtv",
                    "className": "org.droidtv.playtv.PlayTvActivity",
                },
            }
            return await self.setApplication(intent)

        return False

    async def getApplications(self):
        if self.json_feature_supported("applications"):
            r = cast(ApplicationsType, await self.getReq("applications"))
            if r:
                self.applications = {app["id"]: app for app in r["applications"] if "id" in app}
            else:
                self.applications = {}
            return r

    async def getApplication(self):
        if self.json_feature_supported("applications"):
            r = cast(ApplicationIntentType, await self.getReq("activities/current"))
            if r:
                self.application = r
            else:
                self.application = None
            return r

    async def getApplicationIcon(self, id) -> Tuple[Optional[bytes], Optional[str]]:
        if self.json_feature_supported("applications"):
            data, content_type = await self._getBinary(f"applications/{id}/icon")
            return data, content_type
        else:
            return None, None

    async def getPowerState(self):
        r = await self.getReq("powerstate")
        if r:
            self.powerstate = cast(str, r["powerstate"])
        else:
            self.powerstate = None
        return r

    async def setPowerState(self, state):
        data = {"powerstate": state}
        if await self.postReq("powerstate", data) is not None:
            self.powerstate = state
            return True
        return False

    async def getScreenState(self):
        if self.api_version >= 5:
            r = await self.getReq("screenstate")
            if r:
                self.screenstate = cast(str, r["screenstate"])
            else:
                self.screenstate = None
            return r
        else:
            self.screenstate = None

    async def setScreenState(self, state):
        if self.api_version >= 5:
            data = {"screenstate": state}
            if await self.postReq("screenstate", data) is not None:
                self.screenstate = state
                return True
        return False

    async def getHueLampPower(self):
        if self.json_feature_supported("ambilight", "Hue"):
            r = await self.getReq("HueLamp/power")
            if r and "power" in r:
                self.huelamp_power = cast(str, r["power"])
            else:
                self.huelamp_power = None
            return r
        return None

    async def setHueLampPower(self, state):
        if self.json_feature_supported("ambilight", "Hue"):
            data = {"power": state}
            if await self.postReq("HueLamp/power", data) is not None:
                self.huelamp_power = state
                return True
        return False

    async def setApplication(self, intent: ApplicationIntentType):
        if self.json_feature_supported("activities", "intent"):
            data = {"intent": intent}
            if await self.postReq("activities/launch", data) is not None:
                self.application = intent
                return True
        return False

    async def setVolume(self, level, muted=False):
        data = {}
        if self.audio_volume is None or self.min_volume is None or self.max_volume is None:
            await self.getAudiodata()
        assert self.audio_volume is not None
        assert self.max_volume is not None
        assert self.min_volume is not None

        if level is not None:
            try:
                targetlevel = int(level * self.max_volume)
            except ValueError:
                LOG.warning("Invalid audio level %s" % str(level))
                return False
            if targetlevel < self.min_volume or targetlevel > self.max_volume:
                LOG.warning(
                    "Level not in range (%i - %i)" % (self.min_volume, self.max_volume)
                )
                return False
            data["current"] = targetlevel

        data["muted"] = muted

        if await self.postReq("audio/volume", data) is None:
            return False

        self.audio_volume.update(data)

    async def sendKey(self, key):
        res = await self.postReq("input/key", {"key": key}) is not None
        if res:
            if key == "Mute":
                if self.audio_volume:
                    self.audio_volume["muted"] = not self.audio_volume["muted"]
            elif key == "VolumeUp":
                if (
                    self.audio_volume
                    and self.audio_volume["current"] < self.audio_volume["max"]
                ):
                    self.audio_volume["current"] += 1
            elif key == "VolumeDown":
                if (
                    self.audio_volume
                    and self.audio_volume["current"] > self.audio_volume["min"]
                ):
                    self.audio_volume["current"] -= 1

    async def sendUnicode(self, key: str):
        return await self.postReq("input/key", {"unicode": key}) is not None

    async def getAmbilightMode(self):
        data = await self.getReq("ambilight/mode")
        if data:
            self.ambilight_mode_raw = data["current"]

            if self.quirk_ambilight_mode_ignored:
                # we could probably disable quirk here
                if data["current"] != "internal" and self.ambilight_mode_set:
                    LOG.warning(
                        "TV properly report ambilight mode, quirk should be disabled"
                    )
                    self.ambilight_mode_set = None

            return data["current"]

        else:
            self.ambilight_mode_raw = None

    async def setAmbilightMode(self, mode):
        data = {"current": mode}
        if await self.postReq("ambilight/mode", data) is None:
            return False

        if self.quirk_ambilight_mode_ignored:
            if mode == "internal":
                self.ambilight_mode_set = None
                if (
                    await self.postReq(
                        "ambilight/mode", {"current": "internal_invalid"}
                    )
                    is None
                ):
                    LOG.info("Ignoring error for workaround for ambilight mode")
            else:
                self.ambilight_mode_set = mode

        self.ambilight_mode_raw = mode

        return True

    async def getAmbilightTopology(self):
        r = await self.getReq("ambilight/topology")
        if r:
            self.ambilight_topology = r
        else:
            self.ambilight_topology = None
        return r

    async def getAmbilightMeasured(self):
        r = await self.getReq("ambilight/measured")
        if r:
            self.ambilight_measured = r
        else:
            self.ambilight_measured = None
        return r

    async def getAmbilightProcessed(self):
        r = await self.getReq("ambilight/processed")
        if r:
            self.ambilight_processed = r
        else:
            self.ambilight_processed = None
        return r

    async def getAmbilightCached(self):
        """Grab cached ambilight data from device. There are some unconfirmed reports where
        it seems the server crashes while grabbing this data from time to time. So use
        sparingly.
        """
        r = await self.getReq("ambilight/cached")
        if r:
            self.ambilight_cached = r
        else:
            self.ambilight_cached = None
        return r

    async def getAmbilightPower(self):
        if self.api_version >= 5:
            r = await self.getReq("ambilight/power")
            if r:
                self.ambilight_power_raw = r
            else:
                self.ambilight_power_raw = None
            return r

    async def setAmbilightPower(self, power: str):
        if self.api_version >= 5:
            data = {"power": power}
            if await self.postReq("ambilight/power", data) is None:
                return False
            self.ambilight_power_raw = data

            if self.quirk_ambilight_mode_ignored:
                if power == "On" and "lounge" in self.ambilight_modes:
                    self.ambilight_mode_raw = "lounge"
                    self.ambilight_mode_set = "lounge"

            return True

        if self.api_version == 1:
            if power == "On":
                await self.setAmbilightMode("internal")
            else:
                await self.setAmbilightMode("manual")
                await self.setAmbilightCached({"r": 0, "g": 0, "b": 0})

            return True

    async def setAmbilightCached(self, data):
        if await self.postReq("ambilight/cached", data) is None:
            return False

        # won't do optimistic behavior here since
        # the data format can differ a lot
        await self.getAmbilightCached()

        if self.quirk_ambilight_mode_ignored:
            if self.ambilight_mode_set not in ("manual", "expert"):
                self.ambilight_mode_raw = "manual"
                self.ambilight_mode_set = "manual"

        return True

    async def getAmbilightSupportedStyles(self):
        if self.json_feature_supported("ambilight", "Ambilight"):
            r = cast(
                Optional[AmbilightSupportedStylesType],
                await self.getReq("ambilight/supportedstyles"),
            )
            if r:
                self.ambilight_styles = {
                    style["styleName"]: style for style in r["supportedStyles"] if "styleName" in style
                }

                if self.quirk_ambilight_styles_menuitems:
                    style = self.ambilight_styles.setdefault(
                        "FOLLOW_VIDEO", {"styleName": "FOLLOW_VIDEO"}
                    )
                    style["menuSettings"] = [
                        "STANDARD",
                        "VIVID",
                        "IMMERSIVE",
                        "NATURAL",
                        "GAME",
                    ]

                    style = self.ambilight_styles.setdefault(
                        "FOLLOW_AUDIO", {"styleName": "FOLLOW_AUDIO"}
                    )
                    style["menuSettings"] = [
                        "ENERGY_ADAPTIVE_BRIGHTNESS",
                        "VU_METER",
                        "RANDOM_PIXEL_FLASH",
                    ]

                    if "Lounge light" in self.ambilight_styles:
                        style = self.ambilight_styles["Lounge light"]
                    elif "FOLLOW_COLOR" in self.ambilight_styles:
                        style = self.ambilight_styles["FOLLOW_COLOR"]
                    else:
                        style = self.ambilight_styles.setdefault(
                            "Lounge light", {"styleName": "Lounge light"}
                        )
                    style["menuSettings"] = [
                        "HOT_LAVA",
                        "DEEP_WATER",
                        "FRESH_NATURE",
                        "ISF",
                        "CUSTOM_COLOR",
                    ]
            else:
                self.ambilight_styles = {}
            return r

    async def getAmbilightCurrentConfiguration(self):
        if self.json_feature_supported("ambilight", "Ambilight"):
            r = cast(
                Optional[AmbilightCurrentConfiguration],
                await self.getReq("ambilight/currentconfiguration"),
            )
            if r:
                self.ambilight_current_configuration = r
            else:
                self.ambilight_current_configuration = None
            return r

    async def setAmbilightCurrentConfiguration(
        self, config: AmbilightCurrentConfiguration
    ):
        if self.json_feature_supported("ambilight", "Ambilight"):
            r = await self.postReq("ambilight/currentconfiguration", cast(Dict, config))
            if r is None:
                self.ambilight_current_configuration = None
                return False

            self.ambilight_current_configuration = config

            if self.quirk_ambilight_mode_ignored:
                self.ambilight_mode_set = None

            return True

    async def getRecordings(self):
        #Just known working with API level 6 currently
        if self.api_version == 6:
            if self.json_feature_supported("recordings", "List"):
                r = cast(
                    Optional[RecordingsListed],
                    await self.getReq("recordings/list"),
                )
                if r:
                    self.recordings_list = r
                else:
                    self.recordings_list = None
                return r

    async def openURL(self, url: str):
        if self.json_feature_supported("activities", "browser"):
            r = await self.postReq("activities/browser", {"url": url})
            return r is not None

    async def getStringsCached(self, string_ids: Iterable[str]) -> Union[Dict[str, str], None]:
        """Fetch translations for strings, making sure all items exist."""
        string_ids_wanted = set(string_ids)
        string_ids_missing = string_ids_wanted - self.strings.keys()

        # fetch translations from TV
        if string_ids_missing:
            if (data := await self.getStrings(sorted(string_ids_missing))) is None:
                return None
            self.strings.update(data)

        # make sure untranslated strings is set 1 to 1
        string_ids_missing = string_ids_wanted - set(self.strings.keys())
        for string_id in string_ids_missing:
            self.strings[string_id] = string_id

        return self.strings

    async def getStrings(
        self,
        strings: Iterable[str],
        language: Optional[str] = None,
        country: Optional[str] = None,
        variant: Optional[str] = None,
    ) -> Dict[str, str]:
        res: Dict[str, str] = {}
        for group in chunked_iterator(MAXIMUM_ITEMS_IN_REQUEST, strings):
            data = await self._getStrings(group, language=language, country=country, variant=variant)
            res.update(data)
        return res

    async def _getStrings(
        self,
        strings: Iterable[str],
        language: Optional[str] = None,
        country: Optional[str] = None,
        variant: Optional[str] = None,
    ) -> Dict[str, str]:
        data: StringsRequest = {
            "strings": [{"string_id": string} for string in strings],
            "locale": {
                "language": language or "",
                "country": country or "",
                "variant": variant or "",
            },
        }
        res = cast(Optional[Strings], await self.postReq("strings", data))
        if res:
            return {
                translation["string_id"]: translation["string_translation"]
                for translation in res["translations"]
                if translation["string_translation"]
            }
        return {}

    async def getMenuItemsSettingsStructure(self, force=False) -> Optional[MenuItemsSettingsStructure]:
        if self.json_feature_supported("menuitems", "Setup_Menu") or force:
            r = cast(Optional[MenuItemsSettingsStructure],
                    await self.getReq("menuitems/settings/structure")
            )
            self.settings = r
            return r

    async def getMenuItemsSettingsCurrent(self, node_ids: Iterable[int], force=False) -> Optional[MenuItemsSettingsCurrent]:
        current: MenuItemsSettingsCurrent = {"values": [], "version": 0}
        for group in chunked_iterator(MAXIMUM_ITEMS_IN_REQUEST, node_ids):
            if (data := await self._getMenuItemsSettingsCurrent(group)) is None:
                return None

            current["values"].extend(data["values"])
            if current["version"] == 0:
                current["version"] = data["version"]
        return current

    async def _getMenuItemsSettingsCurrent(self, node_ids: Iterable[int], force=False) -> Optional[MenuItemsSettingsCurrent]:
        if not node_ids:
            return None

        if self.json_feature_supported("menuitems", "Setup_Menu") or force:
            post: MenuItemsSettingsCurrentPost = {
                "nodes": [
                    {
                        "nodeid": node_id
                    }
                    for node_id in node_ids
                ] 
            }
            r = cast(Optional[MenuItemsSettingsCurrent],
                     await self.postReq("menuitems/settings/current", cast(dict, post))
            )
            return r

    async def getMenuItemsSettingsCurrentValue(self, node_ids: List[int], force=False) -> Dict[int, Optional[MenuItemsSettingsCurrentValueValue]]:
            data = await self.getMenuItemsSettingsCurrent(node_ids, force=force)
            res: Dict[int, Optional[MenuItemsSettingsCurrentValueValue]] = {}
            if data:
                for value in data.get("values", {}):
                    value_value = value["value"]

                    # Sometimes the API places the data field outside of the value field.
                    # This seem faulty, so let's move it in.
                    if data := value.get("data"):
                        value_value["data"] = data

                    res[value["value"].get("Nodeid")] = value_value
            for node_id in node_ids:
                if node_id not in res:
                    res[node_id] = None
            return res

    async def postMenuItemsSettingsUpdate(self, post: MenuItemsSettingsUpdate, force=False):
        if self.json_feature_supported("menuitems", "Setup_Menu") or force:
            return await self.postReq("menuitems/settings/update", cast(dict, post))

    async def postMenuItemsSettingsUpdateData(self, value: Dict[int, MenuItemsSettingsUpdateValueData], force=False):
        post: MenuItemsSettingsUpdate = {
            "values": [
                {
                    "value": {
                        "Nodeid": node_id,
                        "data": data
                    },
                }
                for node_id, data in value.items()
            ]
        }
        return await self.postMenuItemsSettingsUpdate(post, force=force)
        

    async def notifyChange(self, timeout=TIMEOUT_NOTIFYREAD):
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
                "menuitems/settings/version": {"version": self.settings_version}
            }
        }

        timeout_ctx = httpx.Timeout(timeout=TIMEOUT, connect=TIMEOUT_CONNECT, read=timeout)
        try:
            result = await self.postReq("notifychange", data=data, timeout=timeout_ctx)
        except ProtocolFailure as err:
            # not uncommon for tv to close connection on the lingering connection
            LOG.debug("Protocol failure from device: %s", repr(err))
            result = False
        except ConnectionFailure as err:
            LOG.debug("Connection failure to device: %s", repr(err))
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

            if "menuitems/settings/version" in result:
                self.settings_version = result["menuitems/settings/version"]["version"]

            return True

        if result is None:
            return None

        return False
