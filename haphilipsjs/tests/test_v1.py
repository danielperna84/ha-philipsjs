import haphilipsjs
import pytest
import requests


SYSTEM = {
	"menulanguage": "English",
	"name": "Philips TV",
	"country": "Sweden",
	"serialnumber": "1234567890",
	"softwareversion": "abcd",
	"model": "55PFL6007T/12"
}

SOURCES = {
    "tv":
    {
        "name": "Watch TV"
    },
    "satellite":
    {
        "name": "Watch satellite"
    },
    "hdmi1":
    {
        "name": "HDMI 1"
    },
    "hdmi2":
    {
        "name": "HDMI 2"
    },
    "hdmi3":
    {
        "name": "HDMI 3"
    },
    "hdmiside":
    {
        "name": "HDMI side"
    },
    "ext1":
    {
        "name": "EXT 1"
    },
    "ext2":
    {
        "name": "EXT 2"
    },
    "ypbpr":
    {
        "name": "Y Pb Pr"
    },
    "vga":
    {
        "name": "VGA"
    }
}

SOURCES_CURRENT = {
    "id": "hdmi1"
}

CHANNELS = {
    "fingerprint-1":
    {
        "preset": "1",
        "name": "Flower",
    },
    "fingerprint-2":
    {
        "preset": "2",
        "name": "Moving Colourbar"
    },
    "fingerprint-3":
    {
        "preset": "12.3",
        "name": "Irdeto scrambled"
    },
    "fingerprint-4":
    {
        "preset": "4",
        "name": "Codec 16:9 scrambled"
    },
}

CHANNELS_CURRENT = {
    "id": "fingerprint-1"
}

CHANNELLISTS = {
    "fingerprint-1":
    {
        "name": "All TV channels",
        "source": "tv",
    },
    "fingerprint-2":
    {
        "name": "Favourite TV channels",
        "source": "tv",
    },
    "fingerprint-3":
    {
        "name": "Radio TV channels",
        "source": "tv",
    },
    "fingerprint-4":
    {
        "name": "Non-radio TV channels",
        "source": "tv",
    },
    "fingerprint-5":
    {
        "name": "All satellite channels",
        "source": "satellite",
    },
    "fingerprint-6":
    {
        "name": "Favourite satellite channels",
        "source": "satellite",
    },
    "fingerprint-7":
    {
        "name": "Radio satellite channels",
        "source": "satellite",
    },
    "fingerprint-8":
    {
        "name": "Non-radio satellite channels",
        "source": "satellite",
    }
}

VOLUME = {
    "muted": False,
    "current": 18,
    "min": 0,
    "max": 60
}

@pytest.fixture
def client_mock(requests_mock):
    client = haphilipsjs.PhilipsTV("127.0.0.1", api_version=1)
    requests_mock.get("http://127.0.0.1:1925/1/system", json=SYSTEM)
    requests_mock.get("http://127.0.0.1:1925/1/sources", json=SOURCES)
    requests_mock.get("http://127.0.0.1:1925/1/sources/current", json=SOURCES_CURRENT)
    requests_mock.get("http://127.0.0.1:1925/1/channels", json=CHANNELS)
    requests_mock.get("http://127.0.0.1:1925/1/channels/current", json=CHANNELS_CURRENT)
    requests_mock.get("http://127.0.0.1:1925/1/audio/volume", json=VOLUME)
    requests_mock.get("http://127.0.0.1:1925/1/channellists", json=CHANNELLISTS)
    yield client

def test_basic_data(client_mock):
    """Test for basic data"""
    client_mock.update()
    assert client_mock.on == True
    assert client_mock.system == SYSTEM
    assert client_mock.sources == SOURCES
    assert client_mock.channels == CHANNELS


def test_current_source_none(client_mock, requests_mock):
    client_mock.update()
    assert client_mock.source_id == "hdmi1"

    requests_mock.get("http://127.0.0.1:1925/1/sources/current", json={})
    client_mock.update()
    assert client_mock.source_id == None


def test_current_channel_none(client_mock, requests_mock):
    client_mock.update()
    assert client_mock.channel_id == "fingerprint-1"

    requests_mock.get("http://127.0.0.1:1925/1/channels/current", json={})
    client_mock.update()
    assert client_mock.channel_id == None


def test_current_channel_with_channellist_prefix(client_mock, requests_mock):
    requests_mock.get("http://127.0.0.1:1925/1/channels/current", json={
        "id": "0_fingerprint-1"
    })
    client_mock.update()
    assert client_mock.channel_id == "fingerprint-1"


def test_get_source_name(client_mock):
    """Verify that we can translate source id to name"""
    client_mock.update()
    assert client_mock.getSourceName("ypbpr") == "Y Pb Pr"
    assert client_mock.getSourceName("invalid_name") == None


def test_get_channel_name(client_mock):
    """Verify that we can translate channel id to name"""
    client_mock.update()
    assert client_mock.getChannelName("fingerprint-3") == "Irdeto scrambled"
    assert client_mock.getChannelName("invalid_name") == None


def test_timeout(client_mock, requests_mock):
    """Test that connect timeouts trigger tv to be considered off"""
    client_mock.update()
    assert client_mock.on == True
    requests_mock.get("http://127.0.0.1:1925/1/sources/current", exc=requests.exceptions.ConnectTimeout)

    client_mock.update()
    assert client_mock.on == False

    requests_mock.get("http://127.0.0.1:1925/1/sources/current", json=SOURCES_CURRENT)

    client_mock.update()
    assert client_mock.on == True


def test_volume(client_mock, requests_mock):
    requests_mock.get("http://127.0.0.1:1925/1/audio/volume", json={
        "muted": True,
        "current": 30,
        "min": 0,
        "max": 60
    })

    client_mock.update()
    assert client_mock.volume == 0.5
    assert client_mock.muted == True

    requests_mock.get("http://127.0.0.1:1925/1/audio/volume", json={
        "muted": False,
        "current": 60,
        "min": 0,
        "max": 60
    })

    client_mock.update()
    assert client_mock.volume == 1.0
    assert client_mock.muted == False

    requests_mock.get("http://127.0.0.1:1925/1/audio/volume", json={
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
    requests_mock.post("http://127.0.0.1:1925/1/audio/volume", json={})

    client_mock.setVolume(0.5)

    assert requests_mock.last_request.url == "http://127.0.0.1:1925/1/audio/volume"
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


def test_set_source(client_mock, requests_mock):
    requests_mock.post("http://127.0.0.1:1925/1/sources/current", json={})

    client_mock.setSource("hdmi2")

    assert requests_mock.last_request.url == "http://127.0.0.1:1925/1/sources/current"
    assert requests_mock.last_request.json() == {
        "id": "hdmi2",
    }


def test_set_channel(client_mock, requests_mock):
    requests_mock.post("http://127.0.0.1:1925/1/channels/current", json={})

    client_mock.setChannel("fingerprint-2")

    assert requests_mock.last_request.url == "http://127.0.0.1:1925/1/channels/current"
    assert requests_mock.last_request.json() == {
        "id": "fingerprint-2",
    }


def test_send_key(client_mock, requests_mock):
    requests_mock.post("http://127.0.0.1:1925/1/input/key", json={})

    client_mock.sendKey("Standby")

    assert requests_mock.last_request.url == "http://127.0.0.1:1925/1/input/key"
    assert requests_mock.last_request.json() == {
        "key": "Standby",
    }


def test_send_key_off(client_mock, requests_mock):
    requests_mock.post("http://127.0.0.1:1925/1/input/key", exc=requests.exceptions.ConnectTimeout)

    with pytest.raises(haphilipsjs.ConnectionFailure):
        client_mock.sendKey("Standby")
