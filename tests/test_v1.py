import httpx
import haphilipsjs
import pytest
import respx
import json
from typing import cast, Dict

from haphilipsjs.data.v1 import (
    AMBILIGHT,
    CHANNELLISTS,
    CHANNELS_CURRENT,
    CHANNELS,
    SOURCES_CURRENT,
    SOURCES,
    SYSTEM,
    VOLUME,
)

@pytest.fixture
async def client_mock(loop):
    with respx.mock:
        client = haphilipsjs.PhilipsTV("127.0.0.1", api_version=1)
        respx.get("http://127.0.0.1:1925/1/system").respond(json=cast(Dict, SYSTEM))
        respx.get("http://127.0.0.1:1925/1/sources").respond(json=SOURCES)
        respx.get("http://127.0.0.1:1925/1/sources/current").respond(json=cast(Dict, SOURCES_CURRENT))
        respx.get("http://127.0.0.1:1925/1/channels").respond(json=CHANNELS)
        respx.get("http://127.0.0.1:1925/1/channels/current").respond(json=cast(Dict, CHANNELS_CURRENT))
        respx.get("http://127.0.0.1:1925/1/audio/volume").respond(json=VOLUME)
        respx.get("http://127.0.0.1:1925/1/channellists").respond(json=CHANNELLISTS)
        respx.get("http://127.0.0.1:1925/1/ambilight/mode").respond(json=AMBILIGHT["mode"])
        respx.get("http://127.0.0.1:1925/1/ambilight/topology").respond(json=AMBILIGHT["topology"])
        respx.get("http://127.0.0.1:1925/1/ambilight/measured").respond(json=AMBILIGHT["measured"])
        respx.get("http://127.0.0.1:1925/1/ambilight/processed").respond(json=AMBILIGHT["processed"])
        respx.get("http://127.0.0.1:1925/1/ambilight/cached").respond(json=AMBILIGHT["cached"])
        yield client
        await client.aclose()

async def test_basic_data(client_mock):
    """Test for basic data"""
    await  client_mock.update()
    assert client_mock.on == True
    assert client_mock.system == SYSTEM
    assert client_mock.sources == SOURCES
    assert client_mock.channels == CHANNELS


async def test_current_source_none(client_mock):
    await client_mock.update()
    assert client_mock.source_id == "hdmi1"

    respx.get("http://127.0.0.1:1925/1/sources/current").respond(json={})
    await client_mock.update()
    assert client_mock.source_id == None


async def test_current_channel_none(client_mock):
    await client_mock.update()
    assert client_mock.channel_id == "fingerprint-1"

    respx.get("http://127.0.0.1:1925/1/channels/current").respond(json={})
    await client_mock.update()
    assert client_mock.channel_id == None


async def test_current_channel_with_channellist_prefix(client_mock):
    respx.get("http://127.0.0.1:1925/1/channels/current").respond(json={
        "id": "0_fingerprint-1"
    })
    await client_mock.update()
    assert client_mock.channel_id == "fingerprint-1"


async def test_get_source_name(client_mock):
    """Verify that we can translate source id to name"""
    await client_mock.update()
    assert await client_mock.getSourceName("ypbpr") == "Y Pb Pr"
    assert await client_mock.getSourceName("invalid_name") == None


async def test_get_channel_name(client_mock):
    """Verify that we can translate channel id to name"""
    await client_mock.update()
    assert await client_mock.getChannelName("fingerprint-3") == "Irdeto scrambled"
    assert await client_mock.getChannelName("invalid_name") == None


async def test_timeout(client_mock):
    """Test that connect timeouts trigger tv to be considered off"""
    await client_mock.update()
    assert client_mock.on == True
    respx.get("http://127.0.0.1:1925/1/sources/current").mock(side_effect=httpx.ConnectTimeout)

    await client_mock.update()
    assert client_mock.on == False

    respx.get("http://127.0.0.1:1925/1/sources/current").respond(json=cast(Dict, SOURCES_CURRENT))

    await client_mock.update()
    assert client_mock.on == True


async def test_volume(client_mock):
    respx.get("http://127.0.0.1:1925/1/audio/volume").respond(json={
        "muted": True,
        "current": 30,
        "min": 0,
        "max": 60
    })

    await client_mock.update()
    assert client_mock.volume == 0.5
    assert client_mock.muted == True

    respx.get("http://127.0.0.1:1925/1/audio/volume").respond(json={
        "muted": False,
        "current": 60,
        "min": 0,
        "max": 60
    })

    await client_mock.update()
    assert client_mock.volume == 1.0
    assert client_mock.muted == False

    respx.get("http://127.0.0.1:1925/1/audio/volume").respond(json={
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
    respx.post("http://127.0.0.1:1925/1/audio/volume").respond(json={})

    await client_mock.setVolume(0.5)

    assert respx.calls[-1].request.url == "http://127.0.0.1:1925/1/audio/volume"
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


async def test_set_source(client_mock):
    respx.post("http://127.0.0.1:1925/1/sources/current").respond(json={})

    await client_mock.setSource("hdmi2")

    assert respx.calls[-1].request.url == "http://127.0.0.1:1925/1/sources/current"
    assert json.loads(respx.calls[-1].request.content) == {
        "id": "hdmi2",
    }


async def test_set_channel(client_mock):
    respx.post("http://127.0.0.1:1925/1/channels/current").respond(json={})

    await client_mock.setChannel("fingerprint-2")

    assert respx.calls[-1].request.url == "http://127.0.0.1:1925/1/channels/current"
    assert json.loads(respx.calls[-1].request.content) == {
        "id": "fingerprint-2",
    }


async def test_send_key(client_mock):
    respx.post("http://127.0.0.1:1925/1/input/key").respond(json={})

    await client_mock.sendKey("Standby")

    assert respx.calls[-1].request.url == "http://127.0.0.1:1925/1/input/key"
    assert json.loads(respx.calls[-1].request.content) == {
        "key": "Standby",
    }


async def test_send_key_off(client_mock):
    respx.post("http://127.0.0.1:1925/1/input/key").mock(side_effect=httpx.ConnectTimeout)

    with pytest.raises(haphilipsjs.ConnectionFailure):
        await client_mock.sendKey("Standby")

async def test_ambilight_mode(client_mock):
    await client_mock.getSystem()

    respx.post("http://127.0.0.1:1925/1/ambilight/mode").respond(json={})
    await client_mock.setAmbilightMode("internal")

    assert respx.calls[-1].request.url == "http://127.0.0.1:1925/1/ambilight/mode"
    assert json.loads(respx.calls[-1].request.content) == {
        "current": "internal",
    }

    assert await client_mock.getAmbilightMode()
    assert client_mock.ambilight_mode == "internal"

    assert await client_mock.setAmbilightMode("manual")
    assert client_mock.ambilight_mode == "manual"

    assert await client_mock.getAmbilightMode()
    assert client_mock.ambilight_mode == "manual"

    assert await client_mock.setAmbilightMode("interal")
    assert await client_mock.getAmbilightMode()


async def test_ambilight_power(client_mock):
    await client_mock.getSystem()

    assert client_mock.ambilight_power == None

    await client_mock.getAmbilightPower()
    assert client_mock.ambilight_power == True

    assert await client_mock.setAmbilightPower(True) is None
    assert await client_mock.setAmbilightPower(False) is None


async def test_ambilight_topology(client_mock):
    assert await client_mock.getAmbilightTopology() == AMBILIGHT["topology"]

async def test_ambilight_measured(client_mock):
    assert await client_mock.getAmbilightMeasured() == AMBILIGHT["measured"]

async def test_ambilight_processed(client_mock):
    assert await client_mock.getAmbilightProcessed() == AMBILIGHT["processed"]

async def test_ambilight_cached(client_mock):
    assert await client_mock.getAmbilightCached() == AMBILIGHT["cached"]

    respx.post("http://127.0.0.1:1925/1/ambilight/cached").respond(json={})

    data = {
        "r": 100,
        "g": 210,
        "b": 30
    }

    await client_mock.setAmbilightCached(data)

    assert respx.calls[-1].request.url == "http://127.0.0.1:1925/1/ambilight/cached"
    assert json.loads(respx.calls[-1].request.content) == data
