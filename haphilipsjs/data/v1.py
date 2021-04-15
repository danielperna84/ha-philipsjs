from typing import cast
from haphilipsjs.typing import (
    ChannelsCurrentType,
    SourcesType,
    SystemType,
    SourceCurrentType,
    ChannelsType,
)


SYSTEM_55PFL6007T: SystemType = {
    "menulanguage": "English",
    "name": "Philips TV",
    "country": "Sweden",
    "serialnumber": "1234567890",
    "softwareversion": "abcd",
    "model": "55PFL6007T/12",
}

SYSTEM_47PFH6309: SystemType = {
    "menulanguage": "Spanish",
    "name": "PHILIPS TV",
    "country": "Spain",
    "nettvversion": "",
    "epgsource": "broadcast",
}

SYSTEM_47PFH6309_ENCRYPTED = cast(
    SystemType,
    {
        **SYSTEM_47PFH6309,
        "serialnumber_encrypted": "bf1BcncGiQyBVS47ZXFWjNXoynlKUNlqDhxQz5ikPEU=",
        "softwareversion_encrypted": "K2kseVsmQFgkd15gKkJ+ao+IN30u9WA8apvZ8LuQYkrUGEcxIhN1tkDM7wnn3V+5",
        "model_encrypted": "K2kseVsmQFgkd15gKkJ+akRXrm2rweXcLkCrwpCecFY=",
        "deviceid_encrypted": "",
    },
)

SYSTEM_47PFH6309_DECRYPTED = cast(
    SystemType,
    {
        **SYSTEM_47PFH6309,
        "serialnumber": "ABCDEFGHIJKLF",
        "softwareversion": "mt5880:TPN141E_010.003.086.128",
        "model": "1_47PFH6309/88",
        "deviceid": "",
    },
)

SYSTEM_65PUS6121: SystemType = {
    "menulanguage": "Dutch",
    "name": "65PUS6121",
    "country": "Netherlands",
    "nettvversion": "4.5.0",
    "epgsource": "broadcast",
    "featuring": {
        "jsonfeatures": {
            "recordings": ["List", "Schedule", "Manage"],
            "ambilight": ["LoungeLight"],
            "textentry": ["context_based", "initial_string_available"],
            "inputkey": ["key", "unicode"],
            "pointer": ["context_based"],
            "activities": ["browser"],
        },
        "systemfeatures": {"tvtype": "consumer", "content": ["dmr", "dms_tad"]},
    },
}

SYSTEM_65PUS6121_ENCRYPTED = cast(
    SystemType,
    {
        **SYSTEM_65PUS6121,
        "serialnumber_encrypted": "bf1BcncGiQyBVS47ZXFWjNXoynlKUNlqDhxQz5ikPEU=",
        "softwareversion_encrypted": "K2kseVsmQFgkd15gKkJ+avGAg/2Fns000yNVcCibCqJc8lV5YE2qHdE/pFg2ib2M",
        "model_encrypted": "K2kseVsmQFgkd15gKkJ+ai592Vkjcax6Xprb+fzv08s=",
        "deviceid_encrypted": "K2kseVsmQFgkd15gKkJ+arY7DmesJhIol3fe863YYY0=",
    },
)

SYSTEM_65PUS6121_DECRYPTED = cast(
    SystemType,
    {
        **SYSTEM_65PUS6121,
        "serialnumber": "ABCDEFGHIJKLF",
        "softwareversion": "mt5891:TPL161E_012.003.039.001",
        "model": "1_65PUS6121/12",
        "deviceid": "54885869",
    },
)

SYSTEM_ENCRYPTED = {
    "55PFL6007T": SYSTEM_55PFL6007T,
    "47PFH6309": SYSTEM_47PFH6309_ENCRYPTED,
    "65PUS6121": SYSTEM_65PUS6121_ENCRYPTED,
}

SYSTEM_DECRYPTED = {
    "55PFL6007T": SYSTEM_55PFL6007T,
    "47PFH6309": SYSTEM_47PFH6309_DECRYPTED,
    "65PUS6121": SYSTEM_65PUS6121_DECRYPTED,
}

SOURCES: SourcesType = {
    "tv": {"name": "Watch TV"},
    "satellite": {"name": "Watch satellite"},
    "hdmi1": {"name": "HDMI 1"},
    "hdmi2": {"name": "HDMI 2"},
    "hdmi3": {"name": "HDMI 3"},
    "hdmiside": {"name": "HDMI side"},
    "ext1": {"name": "EXT 1"},
    "ext2": {"name": "EXT 2"},
    "ypbpr": {"name": "Y Pb Pr"},
    "vga": {"name": "VGA"},
}

SOURCES_CURRENT: SourceCurrentType = {"id": "hdmi1"}

CHANNELS: ChannelsType = {
    "fingerprint-1": {
        "preset": "1",
        "name": "Flower",
    },
    "fingerprint-2": {"preset": "2", "name": "Moving Colourbar"},
    "fingerprint-3": {"preset": "12.3", "name": "Irdeto scrambled"},
    "fingerprint-4": {"preset": "4", "name": "Codec 16:9 scrambled"},
}

CHANNELS_CURRENT: ChannelsCurrentType = {"id": "fingerprint-1"}

CHANNELLISTS = {
    "fingerprint-1": {
        "name": "All TV channels",
        "source": "tv",
    },
    "fingerprint-2": {
        "name": "Favourite TV channels",
        "source": "tv",
    },
    "fingerprint-3": {
        "name": "Radio TV channels",
        "source": "tv",
    },
    "fingerprint-4": {
        "name": "Non-radio TV channels",
        "source": "tv",
    },
    "fingerprint-5": {
        "name": "All satellite channels",
        "source": "satellite",
    },
    "fingerprint-6": {
        "name": "Favourite satellite channels",
        "source": "satellite",
    },
    "fingerprint-7": {
        "name": "Radio satellite channels",
        "source": "satellite",
    },
    "fingerprint-8": {
        "name": "Non-radio satellite channels",
        "source": "satellite",
    },
}

VOLUME = {"muted": False, "current": 18, "min": 0, "max": 60}

AMBILIGHT = {
    "mode": {"current": "internal"},
    "topology": {"layers": 1, "left": 4, "top": 0, "right": 4, "bottom": 0},
    "measured": {
        "layer1": {
            "left": {
                "0": {"r": 56, "g": 43, "b": 40},
                "1": {"r": 94, "g": 81, "b": 77},
                "2": {"r": 76, "g": 70, "b": 60},
                "3": {"r": 43, "g": 37, "b": 26},
            },
            "top": {},
            "right": {
                "0": {"r": 69, "g": 70, "b": 58},
                "1": {"r": 124, "g": 120, "b": 100},
                "2": {"r": 83, "g": 87, "b": 90},
                "3": {"r": 50, "g": 49, "b": 51},
            },
            "bottom": {},
        }
    },
    "processed": {
        "layer1": {
            "left": {
                "0": {"r": 37, "g": 77, "b": 182},
                "1": {"r": 53, "g": 87, "b": 186},
                "2": {"r": 64, "g": 96, "b": 188},
                "3": {"r": 19, "g": 67, "b": 188},
            },
            "top": {},
            "right": {
                "0": {"r": 32, "g": 79, "b": 188},
                "1": {"r": 83, "g": 110, "b": 188},
                "2": {"r": 113, "g": 110, "b": 112},
                "3": {"r": 32, "g": 76, "b": 188},
            },
            "bottom": {},
        }
    },
    "cached": {
        "layer1": {
            "left": {
                "0": {"r": 0, "g": 0, "b": 0},
                "1": {"r": 0, "g": 0, "b": 0},
                "2": {"r": 0, "g": 0, "b": 0},
                "3": {"r": 0, "g": 0, "b": 0},
            },
            "top": {},
            "right": {
                "0": {"r": 0, "g": 0, "b": 0},
                "1": {"r": 0, "g": 0, "b": 0},
                "2": {"r": 0, "g": 0, "b": 0},
                "3": {"r": 0, "g": 0, "b": 0},
            },
            "bottom": {},
        }
    },
}

POWERSTATE_65PUS6121 = {"powerstate": "On"}

POWERSTATE = {"65PUS6121": POWERSTATE_65PUS6121}

CONTEXT_65PUS6121 = {
    "activity": "WatchExtension",
    "menu": "Source Menu",
    "Recording": "Off",
}

CONTEXT = {"65PUS6121": CONTEXT_65PUS6121}
