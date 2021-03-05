import httpx
import haphilipsjs
import pytest
import respx
import json
from typing import NamedTuple, cast, Dict

from haphilipsjs.data.v1 import (
    AMBILIGHT,
    CHANNELLISTS,
    CHANNELS_CURRENT,
    CHANNELS,
    SOURCES_CURRENT,
    SOURCES,
    SYSTEM, SYSTEM_47PFH6309_88_DECRYPTED, SYSTEM_47PFH6309_88_ENCRYPTED,
    VOLUME,
)

class Param(NamedTuple):
    type: str
    base: str

@pytest.fixture(params=["standard", "47PFH6309_88"], name="param")
async def param_fixture(request):
    return Param(request.param, "http://127.0.0.1:1925/1")


@pytest.fixture
async def client_mock(loop, param: Param):
    with respx.mock:
        client = haphilipsjs.PhilipsTV("127.0.0.1", api_version=1)
        if param.type == "47PFH6309_88":
            respx.get(f"{param.base}/system").respond(json=cast(Dict, SYSTEM_47PFH6309_88_ENCRYPTED))
        else:
            respx.get(f"{param.base}/system").respond(json=cast(Dict, SYSTEM))
        respx.get(f"{param.base}/sources").respond(json=SOURCES)
        respx.get(f"{param.base}/sources/current").respond(json=cast(Dict, SOURCES_CURRENT))
        respx.get(f"{param.base}/channels").respond(json=CHANNELS)
        respx.get(f"{param.base}/channels/current").respond(json=cast(Dict, CHANNELS_CURRENT))
        respx.get(f"{param.base}/audio/volume").respond(json=VOLUME)
        respx.get(f"{param.base}/channellists").respond(json=CHANNELLISTS)
        respx.get(f"{param.base}/ambilight/mode").respond(json=AMBILIGHT["mode"])
        respx.get(f"{param.base}/ambilight/topology").respond(json=AMBILIGHT["topology"])
        respx.get(f"{param.base}/ambilight/measured").respond(json=AMBILIGHT["measured"])
        respx.get(f"{param.base}/ambilight/processed").respond(json=AMBILIGHT["processed"])
        respx.get(f"{param.base}/ambilight/cached").respond(json=AMBILIGHT["cached"])
        yield client
        await client.aclose()

async def test_basic_data(client_mock: haphilipsjs.PhilipsTV, param: Param):
    """Test for basic data"""
    await  client_mock.update()
    assert client_mock.on == True
    if param.type == "47PFH6309_88":
        assert client_mock.system == SYSTEM_47PFH6309_88_DECRYPTED
    else:
        assert client_mock.system == SYSTEM
    assert client_mock.sources == SOURCES
    assert client_mock.channels == CHANNELS
    assert client_mock.ambilight_current_configuration is None
    assert client_mock.ambilight_styles == {}

async def test_current_source_none(client_mock, param: Param):
    await client_mock.update()
    assert client_mock.source_id == "hdmi1"

    respx.get(f"{param.base}/sources/current").respond(json={})
    await client_mock.update()
    assert client_mock.source_id == None


async def test_current_channel_none(client_mock, param: Param):
    await client_mock.update()
    assert client_mock.channel_id == "fingerprint-1"

    respx.get(f"{param.base}/channels/current").respond(json={})
    await client_mock.update()
    assert client_mock.channel_id == None


async def test_current_channel_with_channellist_prefix(client_mock, param: Param):
    respx.get(f"{param.base}/channels/current").respond(json={
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


async def test_timeout(client_mock, param: Param):
    """Test that connect timeouts trigger tv to be considered off"""
    await client_mock.update()
    assert client_mock.on == True
    respx.get(f"{param.base}/sources/current").mock(side_effect=httpx.ConnectTimeout)

    await client_mock.update()
    assert client_mock.on == False

    respx.get(f"{param.base}/sources/current").respond(json=cast(Dict, SOURCES_CURRENT))

    await client_mock.update()
    assert client_mock.on == True


async def test_volume(client_mock, param: Param):
    respx.get(f"{param.base}/audio/volume").respond(json={
        "muted": True,
        "current": 30,
        "min": 0,
        "max": 60
    })

    await client_mock.update()
    assert client_mock.volume == 0.5
    assert client_mock.muted == True

    respx.get(f"{param.base}/audio/volume").respond(json={
        "muted": False,
        "current": 60,
        "min": 0,
        "max": 60
    })

    await client_mock.update()
    assert client_mock.volume == 1.0
    assert client_mock.muted == False

    respx.get(f"{param.base}/audio/volume").respond(json={
        "muted": False,
        "current": 0,
        "min": 0,
        "max": 60
    })

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


async def test_set_source(client_mock, param: Param):
    respx.post(f"{param.base}/sources/current").respond(json={})

    await client_mock.setSource("hdmi2")

    assert respx.calls[-1].request.url == f"{param.base}/sources/current"
    assert json.loads(respx.calls[-1].request.content) == {
        "id": "hdmi2",
    }


async def test_set_channel(client_mock, param: Param):
    respx.post(f"{param.base}/channels/current").respond(json={})

    await client_mock.setChannel("fingerprint-2")

    assert respx.calls[-1].request.url == f"{param.base}/channels/current"
    assert json.loads(respx.calls[-1].request.content) == {
        "id": "fingerprint-2",
    }


async def test_send_key(client_mock, param: Param):
    respx.post(f"{param.base}/input/key").respond(json={})

    await client_mock.sendKey("Standby")

    assert respx.calls[-1].request.url == f"{param.base}/input/key"
    assert json.loads(respx.calls[-1].request.content) == {
        "key": "Standby",
    }


async def test_send_key_off(client_mock, param: Param):
    respx.post(f"{param.base}/input/key").mock(side_effect=httpx.ConnectTimeout)

    with pytest.raises(haphilipsjs.ConnectionFailure):
        await client_mock.sendKey("Standby")

async def test_ambilight_mode(client_mock, param: Param):
    await client_mock.getSystem()

    respx.post(f"{param.base}/ambilight/mode").respond(json={})
    await client_mock.setAmbilightMode("internal")

    assert respx.calls[-1].request.url == f"{param.base}/ambilight/mode"
    assert json.loads(respx.calls[-1].request.content) == {
        "current": "internal",
    }

    assert await client_mock.getAmbilightMode()
    assert client_mock.ambilight_mode == "internal"

    assert await client_mock.setAmbilightMode("manual")
    assert client_mock.ambilight_mode == "manual"


async def test_ambilight_power(client_mock: haphilipsjs.PhilipsTV, param: Param):
    respx.post(f"{param.base}/ambilight/cached").respond(json={})
    respx.post(f"{param.base}/ambilight/mode").respond(json={})

    assert client_mock.ambilight_power == None
    await client_mock.update()
    await client_mock.getAmbilightPower()
    await client_mock.getAmbilightCached()
    await client_mock.getAmbilightMode()

    assert client_mock.ambilight_power == "On"

    assert await client_mock.setAmbilightPower("Off")

    assert respx.calls[-2].request.url == f"{param.base}/ambilight/cached"
    assert json.loads(respx.calls[-2].request.content) == {"r": 0, "g": 0, "b": 0}

    assert respx.calls[-1].request.url == f"{param.base}/ambilight/cached"

    assert await client_mock.setAmbilightPower("On")

    assert respx.calls[-1].request.url == f"{param.base}/ambilight/mode"
    assert json.loads(respx.calls[-1].request.content) == {"current": "internal"}



async def test_ambilight_topology(client_mock):
    assert await client_mock.getAmbilightTopology() == AMBILIGHT["topology"]

async def test_ambilight_measured(client_mock):
    assert await client_mock.getAmbilightMeasured() == AMBILIGHT["measured"]

async def test_ambilight_processed(client_mock):
    assert await client_mock.getAmbilightProcessed() == AMBILIGHT["processed"]

async def test_ambilight_cached(client_mock, param: Param):
    assert await client_mock.getAmbilightCached() == AMBILIGHT["cached"]

    respx.post(f"{param.base}/ambilight/cached").respond(json={})

    data = {
        "r": 100,
        "g": 210,
        "b": 30
    }

    await client_mock.setAmbilightCached(data)

    assert respx.calls[-2].request.url == f"{param.base}/ambilight/cached"

    assert respx.calls[-1].request.url == f"{param.base}/ambilight/cached"
    assert json.loads(respx.calls[-2].request.content) == data
