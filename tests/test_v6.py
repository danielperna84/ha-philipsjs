import haphilipsjs
import pytest
import httpx
import respx
import json
from typing import Dict, cast

from haphilipsjs.data.v6 import (
    AMBILIGHT,
    ACTIVITIES_TV, APPLICATIONS,
    CHANNELDB_TV,
    CHANNELDB_TV_CHANNELLISTS_ALL,
    ACTIVITIES_CURRENT,
    CONTEXT,
    POWERSTATE,
    SYSTEM_DECRYPTED,
    SYSTEM_ENCRYPTED,
    VOLUME,
    SCREENSTATE,
)

BASE_URL = "https://127.0.0.1:1926/6"



@pytest.fixture
async def client_mock(loop):
    with respx.mock:
        client = haphilipsjs.PhilipsTV("127.0.0.1", api_version=6, secured_transport=True)
        respx.get(f"{BASE_URL}/system").respond(json=cast(Dict, SYSTEM_ENCRYPTED))
        respx.get(f"{BASE_URL}/channeldb/tv").respond(json=cast(Dict, CHANNELDB_TV))
        respx.get(f"{BASE_URL}/channeldb/tv/channelLists/all").respond(json=cast(Dict, CHANNELDB_TV_CHANNELLISTS_ALL))
        respx.get(f"{BASE_URL}/activities/current").respond(json=cast(Dict, ACTIVITIES_CURRENT))
        respx.get(f"{BASE_URL}/activities/tv").respond(json=ACTIVITIES_TV)
        respx.get(f"{BASE_URL}/applications").respond(json=cast(Dict, APPLICATIONS))
        respx.get(f"{BASE_URL}/powerstate").respond(json=POWERSTATE)
        respx.get(f"{BASE_URL}/screenstate").respond(json=SCREENSTATE)
        respx.get(f"{BASE_URL}/context").respond(json=cast(Dict, CONTEXT))
        respx.get(f"{BASE_URL}/audio/volume").respond(json=VOLUME)
        respx.get(f"{BASE_URL}/ambilight/mode").respond(json=AMBILIGHT["mode"])
        respx.get(f"{BASE_URL}/ambilight/topology").respond(json=AMBILIGHT["topology"])
        respx.get(f"{BASE_URL}/ambilight/measured").respond(json=AMBILIGHT["measured"])
        respx.get(f"{BASE_URL}/ambilight/processed").respond(json=AMBILIGHT["processed"])
        respx.get(f"{BASE_URL}/ambilight/cached").respond(json=AMBILIGHT["cached"])
        yield client
        await client.aclose()

async def test_basic_data(client_mock):
    """Test for basic data"""
    await client_mock.update()
    assert client_mock.on == True
    assert client_mock.system == SYSTEM_DECRYPTED
    assert client_mock.sources == {
        "com.mediatek.tvinput/.hdmi.HDMIInputService/HW5" : {
            "name": "HDMI 1"
        },
        "com.mediatek.tvinput/.hdmi.HDMIInputService/HW6" : {
            "name": "HDMI 2"
        },
        "com.mediatek.tvinput/.hdmi.HDMIInputService/HW7" : {
            "name": "HDMI 3"
        },
        "com.mediatek.tvinput/.hdmi.HDMIInputService/HW8" : {
            "name": "HDMI 4"
        },
    }
    assert client_mock.channels == {
        "1648": {
            "ccid": 1648,
            "preset": "1",
            "name": "Irdeto scrambled"
        },
        "1649":  {
            "ccid": 1649,
            "preset": "2"
        }
    }
    assert client_mock.powerstate == POWERSTATE["powerstate"]
    assert client_mock.screenstate == SCREENSTATE["screenstate"]
    assert client_mock.applications == {
        app["id"]: app for app in APPLICATIONS["applications"]
    }
    assert client_mock.application_id == 'org.droidtv.nettv.market.MarketMainActivity-org.droidtv.nettv.market'


async def test_current_channel_none(client_mock):
    await client_mock.update()
    assert client_mock.channel_id == "1648"

    respx.get(f"{BASE_URL}/activities/tv").respond(json={})
    await client_mock.update()
    assert client_mock.channel_id == None


async def test_get_channel_name(client_mock):
    """Verify that we can translate channel id to name"""
    await client_mock.update()
    assert await client_mock.getChannelName("1648") == "Irdeto scrambled"
    assert await client_mock.getChannelName("balha") == None


async def test_set_source(client_mock):
    """Verify that we can translate channel id to name"""

    route = respx.post(f"{BASE_URL}/activities/launch").respond(json={})
    await client_mock.setSource("com.mediatek.tvinput/.hdmi.HDMIInputService/HW5")
    assert json.loads(route.calls[0].request.content) == {
        "intent": {
            "extras": {
                "uri": "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW5"
            },
            "action": "org.droidtv.playtv.SELECTURI", 
            "component": {
                "packageName":"org.droidtv.playtv",
                "className":"org.droidtv.playtv.PlayTvActivity"
            }
        }
    }


async def test_timeout(client_mock):
    """Test that connect timeouts trigger tv to be considered off"""
    await client_mock.update()
    assert client_mock.on == True
    respx.get(f"{BASE_URL}/audio/volume").mock(side_effect=httpx.ConnectTimeout)

    await client_mock.update()
    assert client_mock.on == False

    respx.get(f"{BASE_URL}/audio/volume").respond(json=VOLUME)

    await client_mock.update()
    assert client_mock.on == True


async def test_volume(client_mock):
    respx.get(f"{BASE_URL}/audio/volume").respond(json={
        "muted": True,
        "current": 30,
        "min": 0,
        "max": 60
    })

    await client_mock.update()
    assert client_mock.volume == 0.5
    assert client_mock.muted == True

    respx.get(f"{BASE_URL}/audio/volume").respond(json={
        "muted": False,
        "current": 60,
        "min": 0,
        "max": 60
    })

    await client_mock.update()
    assert client_mock.volume == 1.0
    assert client_mock.muted == False

    respx.get(f"{BASE_URL}/audio/volume").respond(json={
        "muted": False,
        "current": 0,
        "min": 0,
        "max": 60
    })

    await client_mock.update()
    assert client_mock.volume == 0.0
    assert client_mock.muted == False


async def test_set_volume(client_mock):
    await client_mock.update()
    respx.post(f"{BASE_URL}/audio/volume").respond(json={})

    await client_mock.setVolume(0.5)

    assert respx.calls[-1].request.url == f"{BASE_URL}/audio/volume"
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


async def test_set_channel(client_mock):
    respx.post(f"{BASE_URL}/activities/tv").respond(json={})

    await client_mock.setChannel(1649)

    assert respx.calls[-1].request.url == f"{BASE_URL}/activities/tv"
    assert json.loads(respx.calls[-1].request.content) == {
        "channelList": {
            "id": "alltv"
        },
        "channel": {
            "ccid": 1649
        }
    }


async def test_send_key(client_mock):
    respx.post(f"{BASE_URL}/input/key").respond(json={})

    await client_mock.update()
    await client_mock.sendKey("Standby")

    assert respx.calls[-1].request.url == f"{BASE_URL}/input/key"
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


async def test_send_key_off(client_mock):
    respx.post(f"{BASE_URL}/input/key").mock(side_effect=httpx.ConnectTimeout)

    with pytest.raises(haphilipsjs.ConnectionFailure):
        await client_mock.sendKey("Standby")

async def test_ambilight_mode(client_mock):
    assert await client_mock.getAmbilightMode() == "internal"

    respx.post(f"{BASE_URL}/ambilight/mode").respond(json={})
    await client_mock.setAmbilightMode("manual")

    assert respx.calls[-1].request.url == f"{BASE_URL}/ambilight/mode"
    assert json.loads(respx.calls[-1].request.content) == {
        "current": "manual",
    }

async def test_ambilight_topology(client_mock):
    assert await client_mock.getAmbilightTopology() == AMBILIGHT["topology"]

async def test_ambilight_measured(client_mock):
    assert await client_mock.getAmbilightMeasured() == AMBILIGHT["measured"]

async def test_ambilight_processed(client_mock):
    assert await client_mock.getAmbilightProcessed() == AMBILIGHT["processed"]

async def test_ambilight_cached(client_mock):
    assert await client_mock.getAmbilightCached() == AMBILIGHT["cached"]

    respx.post(f"{BASE_URL}/ambilight/cached").respond(json={})

    data = {
        "r": 100,
        "g": 210,
        "b": 30
    }

    await client_mock.setAmbilightCached(data)

    assert respx.calls[-1].request.url == f"{BASE_URL}/ambilight/cached"
    assert json.loads(respx.calls[-1].request.content) == data

async def test_buggy_json():
    assert haphilipsjs.decode_xtv_json("") == {}
    assert haphilipsjs.decode_xtv_json("}") == {}
    assert haphilipsjs.decode_xtv_json('{,"a":{}}') == {"a": {}}
    assert haphilipsjs.decode_xtv_json('{"a":{},}') == {"a": {}}
    assert haphilipsjs.decode_xtv_json('{"a":{},,,"b":{}}') == {"a": {}, "b": {}}
