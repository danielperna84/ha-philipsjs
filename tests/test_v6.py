import haphilipsjs
import pytest
import httpx
import respx
import json
from typing import Dict, NamedTuple, cast

from haphilipsjs.data.v6 import (
    AMBILIGHT,
    ACTIVITIES_TV,
    AMBILIGHT_CURRENT_CONFIGURATION,
    AMBILIGHT_SUPPORTED_STYLES,
    AMBILIGHT_SUPPORTED_STYLES_EXTENDED,
    APPLICATIONS,
    CHANNELDB_TV_ANDROID,
    CHANNELDB_TV_SAPHI,
    CHANNELDB_TV_CHANNELLISTS_ALL,
    ACTIVITIES_CURRENT,
    CONTEXT,
    POWERSTATE,
    SYSTEM_ANDROID_DECRYPTED,
    SYSTEM_ANDROID_ENCRYPTED,
    SYSTEM_SAPHI_DECRYPTED,
    SYSTEM_SAPHI_ENCRYPTED,
    VOLUME,
    SCREENSTATE,
)

MOCK_ANDROID_SOURCES = {
    "content://android.media.tv/channel": {"name": "Watch TV"},
    "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW5": {
        "name": "HDMI 1"
    },
    "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW6": {
        "name": "HDMI 2"
    },
    "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW7": {
        "name": "HDMI 3"
    },
    "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW8": {
        "name": "HDMI 4"
    },
}

MOCK_SAPHI_SOURCES = {}


class Param(NamedTuple):
    type: str
    base: str


@pytest.fixture(params=["android", "saphi"], name="param")
async def param_fixture(request):
    if request.param == "android":
        return Param(request.param, "https://127.0.0.1:1926/6")
    elif request.param == "saphi":
        return Param(request.param, "http://127.0.0.1:1925/6")
    else:
        raise Exception


@pytest.fixture
async def client_mock(loop, param: Param):
    with respx.mock:
        if param.type == "android":
            respx.get(f"{param.base}/system").respond(
                json=cast(Dict, SYSTEM_ANDROID_ENCRYPTED)
            )
            respx.get(f"{param.base}/channeldb/tv").respond(
                json=cast(Dict, CHANNELDB_TV_ANDROID)
            )
        elif param.type == "saphi":
            respx.get(f"{param.base}/system").respond(
                json=cast(Dict, SYSTEM_SAPHI_ENCRYPTED)
            )
            respx.get(f"{param.base}/channeldb/tv").respond(
                json=cast(Dict, CHANNELDB_TV_SAPHI)
            )
        else:
            raise Exception

        respx.get(f"{param.base}/channeldb/tv/channelLists/all").respond(
            json=cast(Dict, CHANNELDB_TV_CHANNELLISTS_ALL)
        )
        respx.get(f"{param.base}/activities/current").respond(
            json=cast(Dict, ACTIVITIES_CURRENT)
        )
        respx.get(f"{param.base}/activities/tv").respond(json=cast(Dict, ACTIVITIES_TV))
        respx.get(f"{param.base}/applications").respond(json=cast(Dict, APPLICATIONS))
        respx.get(f"{param.base}/powerstate").respond(json=POWERSTATE)
        respx.get(f"{param.base}/screenstate").respond(json=SCREENSTATE)
        respx.get(f"{param.base}/context").respond(json=cast(Dict, CONTEXT))
        respx.get(f"{param.base}/audio/volume").respond(json=VOLUME)
        respx.get(f"{param.base}/ambilight/mode").respond(json=AMBILIGHT["mode"])
        respx.get(f"{param.base}/ambilight/topology").respond(
            json=AMBILIGHT["topology"]
        )
        respx.get(f"{param.base}/ambilight/measured").respond(
            json=AMBILIGHT["measured"]
        )
        respx.get(f"{param.base}/ambilight/processed").respond(
            json=AMBILIGHT["processed"]
        )
        respx.get(f"{param.base}/ambilight/cached").respond(json=AMBILIGHT["cached"])
        respx.get(f"{param.base}/ambilight/power").respond(json={"power": "On"})
        respx.get(f"{param.base}/ambilight/supportedstyles").respond(
            json=cast(Dict, AMBILIGHT_SUPPORTED_STYLES)
        )
        respx.get(f"{param.base}/ambilight/currentconfiguration").respond(
            json=cast(Dict, AMBILIGHT_CURRENT_CONFIGURATION)
        )

        if param.type == "android":
            client = haphilipsjs.PhilipsTV(
                "127.0.0.1", api_version=6, secured_transport=True
            )
        elif param.type == "saphi":
            client = haphilipsjs.PhilipsTV(
                "127.0.0.1", api_version=6, secured_transport=False
            )
        else:
            raise Exception

        yield client
        await client.aclose()


async def test_basic_data(client_mock, param: Param):
    """Test for basic data"""
    await client_mock.update()
    assert client_mock.on == True

    if param.type == "android":
        assert client_mock.system == SYSTEM_ANDROID_DECRYPTED
        assert client_mock.sources == MOCK_ANDROID_SOURCES
        assert client_mock.applications == {
            app["id"]: app for app in APPLICATIONS["applications"] if "id" in app
        }
        assert (
            client_mock.application_id
            == "org.droidtv.nettv.market.MarketMainActivity-org.droidtv.nettv.market"
        )
        assert client_mock.quirk_ambilight_mode_ignored == True
        assert client_mock.os_type == "MSAF_2019_P"

    elif param.type == "saphi":
        assert client_mock.system == SYSTEM_SAPHI_DECRYPTED
        assert client_mock.sources == MOCK_SAPHI_SOURCES
        assert client_mock.applications == {}
        assert client_mock.application_id == None
        assert client_mock.quirk_ambilight_mode_ignored == True
        assert client_mock.os_type == "Linux"

    assert client_mock.channels == {
        "1648": {"ccid": 1648, "preset": "1", "name": "Irdeto scrambled"},
        "1649": {"ccid": 1649, "preset": "2"},
    }
    assert client_mock.powerstate == POWERSTATE["powerstate"]
    assert client_mock.screenstate == SCREENSTATE["screenstate"]


async def test_current_channel_none(client_mock, param):
    await client_mock.update()
    assert client_mock.channel_id == "1648"

    respx.get(f"{param.base}/activities/tv").respond(json={})
    await client_mock.update()
    assert client_mock.channel_id == None


async def test_get_channel_name(client_mock):
    """Verify that we can translate channel id to name"""
    await client_mock.update()
    assert await client_mock.getChannelName("1648") == "Irdeto scrambled"
    assert await client_mock.getChannelName("balha") == None


async def test_set_source(client_mock, param):
    """Verify that we can translate channel id to name"""
    await client_mock.update()

    if param.type == "android":
        route = respx.post(f"{param.base}/activities/launch").respond(json={})
        assert await client_mock.setSource(
            "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW5"
        )
        assert json.loads(route.calls[0].request.content) == {
            "intent": {
                "extras": {
                    "uri": "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW5"
                },
                "action": "org.droidtv.playtv.SELECTURI",
                "component": {
                    "packageName": "org.droidtv.playtv",
                    "className": "org.droidtv.playtv.PlayTvActivity",
                },
            }
        }
    elif param.type == "saphi":
        assert await client_mock.setSource("a") == False


async def test_timeout(client_mock, param):
    """Test that connect timeouts trigger tv to be considered off"""
    await client_mock.update()
    assert client_mock.on == True
    respx.get(f"{param.base}/audio/volume").mock(side_effect=httpx.ConnectTimeout)

    await client_mock.update()
    assert client_mock.on == False

    respx.get(f"{param.base}/audio/volume").respond(json=VOLUME)

    await client_mock.update()
    assert client_mock.on == True


async def test_volume(client_mock, param: Param):
    respx.get(f"{param.base}/audio/volume").respond(
        json={"muted": True, "current": 30, "min": 0, "max": 60}
    )

    await client_mock.update()
    assert client_mock.volume == 0.5
    assert client_mock.muted == True

    respx.get(f"{param.base}/audio/volume").respond(
        json={"muted": False, "current": 60, "min": 0, "max": 60}
    )

    await client_mock.update()
    assert client_mock.volume == 1.0
    assert client_mock.muted == False

    respx.get(f"{param.base}/audio/volume").respond(
        json={"muted": False, "current": 0, "min": 0, "max": 60}
    )

    await client_mock.update()
    assert client_mock.volume == 0.0
    assert client_mock.muted == False


async def test_set_volume(client_mock, param: Param):
    await client_mock.update()
    respx.post(f"{param.base}/audio/volume").respond(json={})

    await client_mock.setVolume(0.5)

    assert respx.calls[-1].request.url == f"{param.base}/audio/volume"
    assert json.loads(respx.calls[-1].request.content) == {
        "muted": False,
        "current": 30,
    }

    await client_mock.setVolume(1.0, True)

    assert json.loads(respx.calls[-1].request.content) == {
        "muted": True,
        "current": 60,
    }

    await client_mock.setVolume(0.0, True)

    assert json.loads(respx.calls[-1].request.content) == {
        "muted": True,
        "current": 0,
    }

    await client_mock.setVolume(None, True)

    assert json.loads(respx.calls[-1].request.content) == {
        "muted": True,
    }


async def test_set_channel(client_mock, param: Param):
    respx.post(f"{param.base}/activities/tv").respond(json={})

    await client_mock.setChannel(1649)

    assert respx.calls[-1].request.url == f"{param.base}/activities/tv"
    assert json.loads(respx.calls[-1].request.content) == {
        "channelList": {"id": "alltv"},
        "channel": {"ccid": 1649},
    }


async def test_send_key(client_mock, param: Param):
    respx.post(f"{param.base}/input/key").respond(json={})

    await client_mock.update()
    await client_mock.sendKey("Standby")

    assert respx.calls[-1].request.url == f"{param.base}/input/key"
    assert json.loads(respx.calls[-1].request.content) == {
        "key": "Standby",
    }

    assert client_mock.audio_volume["muted"] == False
    await client_mock.sendKey("Mute")
    assert client_mock.audio_volume["muted"] == True

    assert client_mock.audio_volume["current"] == 18
    await client_mock.sendKey("VolumeUp")
    assert client_mock.audio_volume["current"] == 19
    await client_mock.sendKey("VolumeDown")
    assert client_mock.audio_volume["current"] == 18


async def test_send_key_off(client_mock, param: Param):
    respx.post(f"{param.base}/input/key").mock(side_effect=httpx.ConnectTimeout)

    with pytest.raises(haphilipsjs.ConnectionFailure):
        await client_mock.sendKey("Standby")


async def test_ambilight_mode(client_mock, param):
    await client_mock.getSystem()

    respx.post(f"{param.base}/ambilight/mode").respond(json={})
    await client_mock.setAmbilightMode("internal")

    if client_mock.quirk_ambilight_mode_ignored:
        assert respx.calls[-2].request.url == f"{param.base}/ambilight/mode"
        assert json.loads(respx.calls[-2].request.content) == {
            "current": "internal",
        }
        assert respx.calls[-1].request.url == f"{param.base}/ambilight/mode"
        assert json.loads(respx.calls[-1].request.content) == {
            "current": "internal_invalid",
        }
    else:
        assert respx.calls[-1].request.url == f"{param.base}/ambilight/mode"
        assert json.loads(respx.calls[-1].request.content) == {
            "current": "internal",
        }

    assert await client_mock.getAmbilightMode()
    assert client_mock.ambilight_mode == "internal"

    assert await client_mock.setAmbilightMode("manual")
    assert client_mock.ambilight_mode == "manual"

    if client_mock.quirk_ambilight_mode_ignored:
        assert await client_mock.getAmbilightMode()
        assert client_mock.ambilight_mode == "manual"

    assert await client_mock.setAmbilightMode("interal")
    assert await client_mock.getAmbilightMode()


async def test_ambilight_power(client_mock, param):
    route = respx.post(f"{param.base}/ambilight/power").respond(json={})

    assert client_mock.ambilight_power == None
    await client_mock.update()
    await client_mock.getAmbilightPower()

    assert client_mock.ambilight_power == "On"

    await client_mock.setAmbilightPower("On")
    assert json.loads(route.calls[0].request.content) == {"power": "On"}

    await client_mock.setAmbilightPower("Off")
    assert json.loads(route.calls[1].request.content) == {"power": "Off"}


async def test_ambilight_topology(client_mock):
    assert await client_mock.getAmbilightTopology() == AMBILIGHT["topology"]


async def test_ambilight_measured(client_mock):
    assert await client_mock.getAmbilightMeasured() == AMBILIGHT["measured"]


async def test_ambilight_processed(client_mock):
    assert await client_mock.getAmbilightProcessed() == AMBILIGHT["processed"]


async def test_ambilight_cached(client_mock, param: Param):
    assert await client_mock.getAmbilightCached() == AMBILIGHT["cached"]

    respx.post(f"{param.base}/ambilight/cached").respond(json={})

    data = {"r": 100, "g": 210, "b": 30}

    await client_mock.setAmbilightCached(data)

    assert respx.calls[-2].request.url == f"{param.base}/ambilight/cached"

    assert respx.calls[-2].request.url == f"{param.base}/ambilight/cached"
    assert json.loads(respx.calls[-2].request.content) == data


async def test_ambilight_modes(client_mock, param):
    await client_mock.getSystem()
    if param.type == "android":
        assert client_mock.ambilight_modes == ["internal", "manual", "expert", "lounge"]
    elif param.type == "saphi":
        assert client_mock.ambilight_modes == ["internal", "manual", "expert"]


async def test_ambilight_current_configuration(client_mock, param):
    respx.post(f"{param.base}/ambilight/currentconfiguration").respond(json={})

    await client_mock.getSystem()
    await client_mock.getAmbilightCurrentConfiguration()

    data = {
        "isExpert": False,
        "menuSetting": "STANDARD",
        "stringValue": "Standard",
        "styleName": "FOLLOW_VIDEO",
    }

    assert client_mock.ambilight_current_configuration == data

    await client_mock.setAmbilightCurrentConfiguration(data)
    assert json.loads(respx.calls[-1].request.content) == data


async def test_ambilight_supported_stypes(client_mock, param):
    await client_mock.getSystem()
    await client_mock.getAmbilightSupportedStyles()
    assert client_mock.ambilight_styles == AMBILIGHT_SUPPORTED_STYLES_EXTENDED[param.type]


async def test_buggy_json():
    assert haphilipsjs.decode_xtv_json("") == {}
    assert haphilipsjs.decode_xtv_json("}") == {}
    assert haphilipsjs.decode_xtv_json('{,"a":{}}') == {"a": {}}
    assert haphilipsjs.decode_xtv_json('{"a":{},}') == {"a": {}}
    assert haphilipsjs.decode_xtv_json('{"a":{},,,"b":{}}') == {"a": {}, "b": {}}
