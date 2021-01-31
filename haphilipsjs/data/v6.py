SYSTEM = {
    "menulanguage": "Dutch",
    "name": "55PUS7181\/12",
    "country": "Netherlands",
    "serialnumber_encrypted": "F6905Z+vyquNhZoXegQ1DzZXCqMIcjJpkzy3LsiPac=\n",
    "softwareversion_encrypted": "1YWR42sjQ6xdjuyIXWZbyPnoRswLoRswLmKtAhR9GRsBx1qY=\n",
    "model_encrypted": "jGNvXDerdJoWjOpwh\/n0gw2MgM7oRswLoRswLKC73wfMgra3S62c4=\n",
    "deviceid_encrypted": "7mv3ZEtMH8oRswL0RoRswLISTn38FN8HAqfmSF95qoaiRsuukSraQ=\n",
    "nettvversion": "6.0.2",
    "epgsource": "one",
    "api_version": {"Major": 6, "Minor": 2, "Patch": 0},
    "featuring": {
        "jsonfeatures": {
            "editfavorites": ["TVChannels", "SatChannels"],
            "recordings": ["List", "Schedule", "Manage"],
            "ambilight": ["LoungeLight", "Hue", "Ambilight"],
            "menuitems": ["Setup_Menu"],
            "textentry": [
                "context_based",
                "initial_string_available",
                "editor_info_available",
            ],
            "applications": ["TV_Apps", "TV_Games", "TV_Settings"],
            "pointer": ["not_available"],
            "inputkey": ["key"],
            "activities": ["intent"],
            "channels": ["preset_string"],
            "mappings": ["server_mapping"],
        },
        "systemfeatures": {
            "tvtype": "consumer",
            "content": ["dmr", "dms_tad"],
            "tvsearch": "intent",
            "pairing_type": "digest_auth_pairing",
            "secured_transport": "True",
        },
    },
}

VOLUME = {"muted": False, "current": 18, "min": 0, "max": 60}

ACTIVITIES_CURRENT = {
    "component": {
        "packageName": "org.droidtv.nettv.market",
        "className": "org.droidtv.nettv.market.MarketMainActivity",
    }
}

ACTIVITIES_TV = {
    "channel": {
        "ccid": 1648
    }
}

CHANNELDB_TV_CHANNELLISTS_ALL = {
    "id": "all",
    "version": 10,
    "listType": "MixedSources",
    "medium": "mixed",
    "active": True,
    "virtual": True,
    "modifiable": False,
    "Channel": [
        {"ccid": 1648, "preset": "1", "name": "Irdeto scrambled"},
        {"ccid": 1649, "preset": "2"},
    ],
}

CHANNELDB_TV = {
    "channelLists": [CHANNELDB_TV_CHANNELLISTS_ALL],
    "favoriteLists": [
        {
            "id": "com.google.android.videos%2F.tv.usecase.tvinput.playback.TvInputService",
            "version": 1545826184134,
            "parentId": "all",
            "listType": "MixedSources",
            "medium": "mixed",
            "virtual": False,
            "modifiable": False,
            "name": "Google Play Movies & TV",
        },
        {
            "id": "1",
            "version": "0",
            "listType": "MixedSources",
            "medium": "mixed",
            "name": "Favourites 1",
            "parentId": "all",
            "virtual": False,
            "modifiable": True,
        },
    ],
}


AMBILIGHT = {
    "mode": {"current": "internal"},
    "currentconfiguration": {
        "styleName": "FOLLOW_VIDEO",
        "isExpert": False,
        "menuSetting": "STANDARD",
    },
    "lounge": {
        "color": {"hue": 0, "saturation": 0, "brightness": 0},
        "colordelta": {"hue": 0, "saturation": 0, "brightness": 0},
        "speed": 0,
        "mode": "Default",
    },
    "power": {"power": "On"},
    "supportedstyles": {
        "supportedStyles": [
            {"styleName": "OFF"},
            {"styleName": "FOLLOW_VIDEO"},
            {
                "styleName": "FOLLOW_AUDIO",
                "algorithms": [
                    "ENERGY_ADAPTIVE_BRIGHTNESS",
                    "ENERGY_ADAPTIVE_COLORS",
                    "VU_METER",
                    "SPECTRUM_ANALYZER",
                    "KNIGHT_RIDER_CLOCKWISE",
                    "KNIGHT_RIDER_ALTERNATING",
                    "RANDOM_PIXEL_FLASH",
                    "STROBO",
                    "PARTY",
                ],
                "maxTuning": 2,
            },
            {
                "styleName": "FOLLOW_COLOR",
                "algorithms": ["MANUAL_HUE", "AUTOMATIC_HUE"],
                "maxSpeed": 255,
            },
            {"styleName": "LOUNGE"},
            {"styleName": "MANUAL"},
            {"styleName": "EXPERT"},
            {"styleName": "GRID"},
        ]
    },
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
