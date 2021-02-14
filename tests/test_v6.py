import haphilipsjs
import pytest
import requests

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
def client_mock(requests_mock):
    client = haphilipsjs.PhilipsTV("127.0.0.1", api_version=6, secured_transport=True)
    requests_mock.get(f"{BASE_URL}/system", json=SYSTEM_ENCRYPTED)
    requests_mock.get(f"{BASE_URL}/channeldb/tv", json=CHANNELDB_TV)
    requests_mock.get(f"{BASE_URL}/channeldb/tv/channelLists/all", json=CHANNELDB_TV_CHANNELLISTS_ALL)
    requests_mock.get(f"{BASE_URL}/activities/current", json=ACTIVITIES_CURRENT)
    requests_mock.get(f"{BASE_URL}/activities/tv", json=ACTIVITIES_TV)
    requests_mock.get(f"{BASE_URL}/applications", json=APPLICATIONS)
    requests_mock.get(f"{BASE_URL}/powerstate", json=POWERSTATE)
    requests_mock.get(f"{BASE_URL}/screenstate", json=SCREENSTATE)
    requests_mock.get(f"{BASE_URL}/context", json=CONTEXT)
    requests_mock.get(f"{BASE_URL}/audio/volume", json=VOLUME)
    requests_mock.get(f"{BASE_URL}/ambilight/mode", json=AMBILIGHT["mode"])
    requests_mock.get(f"{BASE_URL}/ambilight/topology", json=AMBILIGHT["topology"])
    requests_mock.get(f"{BASE_URL}/ambilight/measured", json=AMBILIGHT["measured"])
    requests_mock.get(f"{BASE_URL}/ambilight/processed", json=AMBILIGHT["processed"])
    requests_mock.get(f"{BASE_URL}/ambilight/cached", json=AMBILIGHT["cached"])
    yield client

def test_basic_data(client_mock):
    """Test for basic data"""
    client_mock.update()
    assert client_mock.on == True
    assert client_mock.system == SYSTEM_DECRYPTED
    assert client_mock.sources is None
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
    assert client_mock.applications == APPLICATIONS


def test_current_channel_none(client_mock, requests_mock):
    client_mock.update()
    assert client_mock.channel_id == "1648"

    requests_mock.get(f"{BASE_URL}/activities/tv", json={})
    client_mock.update()
    assert client_mock.channel_id == None


def test_get_channel_name(client_mock):
    """Verify that we can translate channel id to name"""
    client_mock.update()
    assert client_mock.getChannelName("1648") == "Irdeto scrambled"
    assert client_mock.getChannelName("balha") == None


def test_timeout(client_mock, requests_mock):
    """Test that connect timeouts trigger tv to be considered off"""
    client_mock.update()
    assert client_mock.on == True
    requests_mock.get(f"{BASE_URL}/audio/volume", exc=requests.exceptions.ConnectTimeout)

    client_mock.update()
    assert client_mock.on == False

    requests_mock.get(f"{BASE_URL}/audio/volume", json=VOLUME)

    client_mock.update()
    assert client_mock.on == True


def test_volume(client_mock, requests_mock):
    requests_mock.get(f"{BASE_URL}/audio/volume", json={
        "muted": True,
        "current": 30,
        "min": 0,
        "max": 60
    })

    client_mock.update()
    assert client_mock.volume == 0.5
    assert client_mock.muted == True

    requests_mock.get(f"{BASE_URL}/audio/volume", json={
        "muted": False,
        "current": 60,
        "min": 0,
        "max": 60
    })

    client_mock.update()
    assert client_mock.volume == 1.0
    assert client_mock.muted == False

    requests_mock.get(f"{BASE_URL}/audio/volume", json={
        "muted": False,
        "current": 0,
        "min": 0,
        "max": 60
    })

    client_mock.update()
    assert client_mock.volume == 0.0
    assert client_mock.muted == False


def test_set_volume(client_mock, requests_mock):
    client_mock.update()
    requests_mock.post(f"{BASE_URL}/audio/volume", json={})

    client_mock.setVolume(0.5)

    assert requests_mock.last_request.url == f"{BASE_URL}/audio/volume"
    assert requests_mock.last_request.json() == {
        "muted": False,
        "current": 30,
    }

    client_mock.setVolume(1.0, True)

    assert requests_mock.last_request.json() == {
        "muted": True,
        "current": 60,
    }

    client_mock.setVolume(0.0, True)

    assert requests_mock.last_request.json() == {
        "muted": True,
        "current": 0,
    }

    client_mock.setVolume(None, True)

    assert requests_mock.last_request.json() == {
        "muted": True,
    }


def test_set_channel(client_mock, requests_mock):
    requests_mock.post(f"{BASE_URL}/activities/tv", json={})

    client_mock.setChannel(1649)

    assert requests_mock.last_request.url == f"{BASE_URL}/activities/tv"
    assert requests_mock.last_request.json() == {
        "channelList": {
            "id": "alltv"
        },
        "channel": {
            "ccid": 1649
        }
    }


def test_send_key(client_mock, requests_mock):
    requests_mock.post(f"{BASE_URL}/input/key", json={})

    client_mock.update()
    client_mock.sendKey("Standby")

    assert requests_mock.last_request.url == f"{BASE_URL}/input/key"
    assert requests_mock.last_request.json() == {
        "key": "Standby",
    }

    assert client_mock.audio_volume["muted"] == False
    client_mock.sendKey("Mute")
    assert client_mock.audio_volume["muted"] == True

    assert client_mock.audio_volume["current"] == 18
    client_mock.sendKey("VolumeUp")
    assert client_mock.audio_volume["current"] == 19
    client_mock.sendKey("VolumeDown")
    assert client_mock.audio_volume["current"] == 18


def test_send_key_off(client_mock, requests_mock):
    requests_mock.post(f"{BASE_URL}/input/key", exc=requests.exceptions.ConnectTimeout)

    with pytest.raises(haphilipsjs.ConnectionFailure):
        client_mock.sendKey("Standby")

def test_ambilight_mode(client_mock, requests_mock):
    assert client_mock.getAmbilightMode() == "internal"

    requests_mock.post(f"{BASE_URL}/ambilight/mode", json={})
    client_mock.setAmbilightMode("manual")

    assert requests_mock.last_request.url == f"{BASE_URL}/ambilight/mode"
    assert requests_mock.last_request.json() == {
        "current": "manual",
    }

def test_ambilight_topology(client_mock):
    assert client_mock.getAmbilightTopology() == AMBILIGHT["topology"]

def test_ambilight_measured(client_mock):
    assert client_mock.getAmbilightMeasured() == AMBILIGHT["measured"]

def test_ambilight_processed(client_mock):
    assert client_mock.getAmbilightProcessed() == AMBILIGHT["processed"]

def test_ambilight_cached(client_mock, requests_mock):
    assert client_mock.getAmbilightCached() == AMBILIGHT["cached"]

    requests_mock.post(f"{BASE_URL}/ambilight/cached", json={})

    data = {
        "r": 100,
        "g": 210,
        "b": 30
    }

    client_mock.setAmbilightCached(data)

    assert requests_mock.last_request.url == f"{BASE_URL}/ambilight/cached"
    assert requests_mock.last_request.json() == data

def test_buggy_json():
    assert haphilipsjs.decode_xtv_json("") == {}
    assert haphilipsjs.decode_xtv_json("}") == {}
    assert haphilipsjs.decode_xtv_json('{,"a":{}}') == {"a": {}}
    assert haphilipsjs.decode_xtv_json('{"a":{},}') == {"a": {}}
    assert haphilipsjs.decode_xtv_json('{"a":{},,,"b":{}}') == {"a": {}, "b": {}}
