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

AMBILIGHT = {
    "mode": {
        "current": "internal"
    },
    "topology": {
        "layers": 1,
        "left": 4,
        "top": 0,
        "right": 4,
        "bottom": 0
    },
    "measured": {
        "layer1": {
            "left": {
                "0": {
                    "r": 56,
                    "g": 43,
                    "b": 40
                },
                "1": {
                    "r": 94,
                    "g": 81,
                    "b": 77
                },
                "2": {
                    "r": 76,
                    "g": 70,
                    "b": 60
                },
                "3": {
                    "r": 43,
                    "g": 37,
                    "b": 26
                }
            },
            "top": {

            },
            "right": {
                "0": {
                    "r": 69,
                    "g": 70,
                    "b": 58
                },
                "1": {
                    "r": 124,
                    "g": 120,
                    "b": 100
                },
                "2": {
                    "r": 83,
                    "g": 87,
                    "b": 90
                },
                "3": {
                    "r": 50,
                    "g": 49,
                    "b": 51
                }
            },
            "bottom": {

            }
        }
    },
    "processed": {
        "layer1": {
            "left": {
                "0": {
                    "r": 37,
                    "g": 77,
                    "b": 182
                },
                "1": {
                    "r": 53,
                    "g": 87,
                    "b": 186
                },
                "2": {
                    "r": 64,
                    "g": 96,
                    "b": 188
                },
                "3": {
                    "r": 19,
                    "g": 67,
                    "b": 188
                }
            },
            "top": {

            },
            "right": {
                "0": {
                    "r": 32,
                    "g": 79,
                    "b": 188
                },
                "1": {
                    "r": 83,
                    "g": 110,
                    "b": 188
                },
                "2": {
                    "r": 113,
                    "g": 110,
                    "b": 112
                },
                "3": {
                    "r": 32,
                    "g": 76,
                    "b": 188
                }
            },
            "bottom": {

            }
        }
    },
    "cached": {
        "layer1": {
            "left": {
                "0": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                },
                "1": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                },
                "2": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                },
                "3": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                }
            },
            "top": {

            },
            "right": {
                "0": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                },
                "1": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                },
                "2": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                },
                "3": {
                    "r": 0,
                    "g": 0,
                    "b": 0
                }
            },
            "bottom": {

            }
        }
    }
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
    requests_mock.get("http://127.0.0.1:1925/1/ambilight/mode", json=AMBILIGHT["mode"])
    requests_mock.get("http://127.0.0.1:1925/1/ambilight/topology", json=AMBILIGHT["topology"])
    requests_mock.get("http://127.0.0.1:1925/1/ambilight/measured", json=AMBILIGHT["measured"])
    requests_mock.get("http://127.0.0.1:1925/1/ambilight/processed", json=AMBILIGHT["processed"])
    requests_mock.get("http://127.0.0.1:1925/1/ambilight/cached", json=AMBILIGHT["cached"])
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

def test_ambilight_mode(client_mock, requests_mock):
    assert client_mock.getAmbilightMode() == "internal"

    requests_mock.post("http://127.0.0.1:1925/1/ambilight/mode", json={})
    client_mock.setAmbilightMode("manual")

    assert requests_mock.last_request.url == "http://127.0.0.1:1925/1/ambilight/mode"
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

    requests_mock.post("http://127.0.0.1:1925/1/ambilight/cached", json={})

    data = {
        "r": 100,
        "g": 210,
        "b": 30
    }

    client_mock.setAmbilightCached(data)

    assert requests_mock.last_request.url == "http://127.0.0.1:1925/1/ambilight/cached"
    assert requests_mock.last_request.json() == data
