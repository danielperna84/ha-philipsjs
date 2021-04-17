from typing import cast, Dict
from haphilipsjs.typing import (
    ActivitesTVType,
    AmbilightCurrentConfiguration,
    AmbilightSupportedStylesType,
    AmbilightSupportedStyleType,
    ApplicationIntentType,
    ApplicationsType,
    ChannelDbTv,
    ChannelListType,
    ComponentType,
    ContextType,
    FavoriteListType,
    SystemType,
)


SYSTEM_ANDROID: SystemType = {
    "notifyChange": "http",
    "menulanguage": "Swedish",
    "name": "65OLED855/12",
    "country": "Sweden",
    "nettvversion": "9.0.0",
    "epgsource": "broadcast",
    "api_version": {"Major": 6, "Minor": 4, "Patch": 0},
    "featuring": {
        "jsonfeatures": {
            "editfavorites": ["TVChannels", "SatChannels"],
            "recordings": ["List", "Schedule", "Manage"],
            "ambilight": ["LoungeLight", "Hue", "Ambilight", "HueStreaming"],
            "menuitems": ["Setup_Menu"],
            "textentry": ["not_available"],
            "applications": ["TV_Apps", "TV_Games", "TV_Settings"],
            "pointer": ["not_available"],
            "inputkey": ["key"],
            "activities": ["intent"],
            "channels": ["preset_string"],
            "mappings": ["server_mapping"],
        },
        "systemfeatures": {
            "tvtype": "consumer",
            "content": ["dmr", "pvr"],
            "tvsearch": "intent",
            "pairing_type": "digest_auth_pairing",
            "secured_transport": "true",
            "companion_screen": "true",
        },
    },
    "os_type": "MSAF_2019_P",
}

SYSTEM_ANDROID_ENCRYPTED = cast(
    SystemType,
    {
        **SYSTEM_ANDROID,
        "serialnumber_encrypted": "bf1BcncGiQyBVS47ZXFWjNXoynlKUNlqDhxQz5ikPEU=\n",
        "softwareversion_encrypted": "o5VTq/nnyhUzdpj+ac65ItwU2KTv6j6bu8brxNxA+5J78u9D7fdZwqcAilvhFc9L\n",
        "model_encrypted": "3Cdh9HfKdQZb0UJPzeXau15tgTFcLdYcPGb0NqOreDg=\n",
        "deviceid_encrypted": "0dwhYxbc4pu9bo+yXXKsSaAI/GqIoxSMlQIs6osKlCI=\n",
    },
)

SYSTEM_ANDROID_DECRYPTED = cast(
    SystemType,
    {
        **SYSTEM_ANDROID,
        "serialnumber": "ABCDEFGHIJKLF",
        "softwareversion": "TPM191E_R.101.001.208.001",
        "model": "65OLED855/12",
        "deviceid": "1234567890",
    },
)

SYSTEM_SAPHI: SystemType = {
    "menulanguage": "Dutch",
    "name": "50PUS6804/12",
    "country": "Netherlands",
    "nettvversion": "4.6.0.1",
    "epgsource": "no_epg",
    "api_version": {"Major": 6, "Minor": 1, "Patch": 0},
    "featuring": {
        "jsonfeatures": {
            "recordings": ["List", "Schedule", "Manage"],
            "ambilight": ["Hue", "HueStreaming", "Ambilight"],
            "textentry": ["context_based", "initial_string_available"],
            "inputkey": ["key", "unicode"],
            "pointer": ["context_based"],
            "activities": ["browser"],
        },
        "systemfeatures": {
            "tvtype": "consumer",
            "content": ["dmr"],
            "pairing_type": "none",
            "companion_screen": True,
            "os_type": "Linux",
        },
    },
}

SYSTEM_SAPHI_ENCRYPTED = cast(
    SystemType,
    {
        **SYSTEM_SAPHI,
        "serialnumber_encrypted": "bf1BcncGiQyBVS47ZXFWjNXoynlKUNlqDhxQz5ikPEU=\n",
        "softwareversion_encrypted": "K2kseVsmQFgkd15gKkJ+amueMe3DHAmDQ8d/R/pbq75SQ3mIJ7KzpbV8Z0lz4DAg",
        "model_encrypted": "K2kseVsmQFgkd15gKkJ+ajj14v1k18xtrm2jX61cQ9Y=",
        "deviceid_encrypted": "0dwhYxbc4pu9bo+yXXKsSaAI/GqIoxSMlQIs6osKlCI=\n",
    },
)

SYSTEM_SAPHI_DECRYPTED = cast(
    SystemType,
    {
        **SYSTEM_SAPHI,
        "serialnumber": "ABCDEFGHIJKLF",
        "softwareversion": "mt5887:TPM196E_091.003.255.001",
        "model": "1_50PUS6804/12",
        "deviceid": "1234567890",
    },
)


VOLUME = {"muted": False, "current": 18, "min": 0, "max": 60}

APPLICATIONS: ApplicationsType = {
    "version": 0,
    "applications": [
        {
            "label": "Så här......",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.eum",
                    "className": "org.droidtv.eum.onehelp.HowToTutorials.HowToVideosActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "org.droidtv.eum.onehelp.HowToTutorials.HowToVideosActivity-org.droidtv.eum",
            "type": "app",
        },
        {
            "label": "Play Butik",
            "intent": {
                "component": {
                    "packageName": "com.android.vending",
                    "className": "com.google.android.finsky.tvmainactivity.TvMainActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "com.google.android.finsky.tvmainactivity.TvMainActivity-com.android.vending",
            "type": "app",
        },
        {
            "label": "YouTube",
            "intent": {
                "component": {
                    "packageName": "com.google.android.youtube.tv",
                    "className": "com.google.android.apps.youtube.tv.activity.ShellActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "com.google.android.apps.youtube.tv.activity.ShellActivity-com.google.android.youtube.tv",
            "type": "app",
        },
        {
            "label": "TED",
            "intent": {
                "component": {
                    "packageName": "com.ted.android.tv",
                    "className": "com.ted.android.tv.view.MainActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "com.ted.android.tv.view.MainActivity-com.ted.android.tv",
            "type": "app",
        },
        {
            "label": "Play Spel",
            "intent": {
                "component": {
                    "packageName": "com.google.android.play.games",
                    "className": "com.google.android.apps.play.games.app.atv.features.home.HomeActivity",
                },
                "action": "empty",
            },
            "order": 0,
            "id": "com.google.android.apps.play.games.app.atv.features.home.HomeActivity-com.google.android.play.games",
            "type": "app",
        },
        {
            "label": "Netflix",
            "intent": {
                "component": {
                    "packageName": "com.netflix.ninja",
                    "className": "com.netflix.ninja.MainActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "com.netflix.ninja.MainActivity-com.netflix.ninja",
            "type": "app",
        },
        {
            "label": "Amazon Alexa",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.amazonalexa",
                    "className": "org.droidtv.amazonalexa.wizard.AlexaWizardActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "org.droidtv.amazonalexa.wizard.AlexaWizardActivity-org.droidtv.amazonalexa",
            "type": "app",
        },
        {
            "label": "TV-guide",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.channels",
                    "className": "org.droidtv.channels.ChannelsActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "org.droidtv.channels.ChannelsActivity-org.droidtv.channels",
            "type": "app",
        },
        {
            "label": "Media",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.contentexplorer",
                    "className": "org.droidtv.contentexplorer.MainActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "org.droidtv.contentexplorer.MainActivity-org.droidtv.contentexplorer",
            "type": "app",
        },
        {
            "label": "Demo Me",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.demome",
                    "className": "org.droidtv.demome.DemoMeOptionsActivity",
                },
                "action": "empty",
            },
            "order": 0,
            "id": "org.droidtv.demome.DemoMeOptionsActivity-org.droidtv.demome",
            "type": "app",
        },
        {
            "label": "Philips TV-samling",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.nettv.market",
                    "className": "org.droidtv.nettv.market.MarketMainActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "org.droidtv.nettv.market.MarketMainActivity-org.droidtv.nettv.market",
            "type": "app",
        },
        {
            "label": "Toppval",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.nettvrecommender",
                    "className": "org.droidtv.nettvrecommender.NetTvRecommenderMainActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "org.droidtv.nettvrecommender.NetTvRecommenderMainActivity-org.droidtv.nettvrecommender",
            "type": "app",
        },
        {
            "label": "TV",
            "intent": {
                "component": {
                    "packageName": "org.droidtv.playtv",
                    "className": "org.droidtv.playtv.PlayTvActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "org.droidtv.playtv.PlayTvActivity-org.droidtv.playtv",
            "type": "app",
        },
        {
            "label": "Viafree",
            "intent": {
                "component": {
                    "packageName": "se.viafree.android",
                    "className": "com.viafree.android.SplashActivity",
                },
                "action": "android.intent.action.MAIN",
            },
            "order": 0,
            "id": "com.viafree.android.SplashActivity-se.viafree.android",
            "type": "app",
        },
    ],
}

ACTIVITIES_CURRENT: ApplicationIntentType = {
    "component": {
        "packageName": "org.droidtv.nettv.market",
        "className": "org.droidtv.nettv.market.MarketMainActivity",
    }
}

ACTIVITIES_TV: ActivitesTVType = {"channel": {"ccid": 1648}}

CHANNELDB_TV_CHANNELLISTS_ALL: ChannelListType = {
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

CHANNELDB_TV_ANDROID: ChannelDbTv = {
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


CHANNELDB_TV_SAPHI: ChannelDbTv = {
    "channelLists": [CHANNELDB_TV_CHANNELLISTS_ALL],
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
    "power": {"power": "On"},
}

AMBILIGHT_SUPPORTED_STYLES: AmbilightSupportedStylesType = {
    "supportedStyles": [
        {},
        {},
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
            "styleName": "Lounge light",
            "algorithms": ["MANUAL_HUE", "AUTOMATIC_HUE"],
            "maxSpeed": 255,
        },
        {},
        {},
        {},
        {},
        {},
        {},
    ]
}

AMBILIGHT_SUPPORTED_STYLES_EXTENDED_ANDROID: Dict[str, AmbilightSupportedStyleType] = {
    "FOLLOW_VIDEO": {
        "styleName": "FOLLOW_VIDEO",
        "menuSettings": ["STANDARD", "VIVID", "IMMERSIVE", "NATURAL", "GAME"],
    },
    "FOLLOW_AUDIO": {
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
        "menuSettings": ["ENERGY_ADAPTIVE_BRIGHTNESS", "VU_METER", "RANDOM_PIXEL_FLASH"],
        "maxTuning": 2,
    },
    "Lounge light": {
        "styleName": "Lounge light",
        "algorithms": ["MANUAL_HUE", "AUTOMATIC_HUE"],
        "menuSettings": [
            "HOT_LAVA",
            "DEEP_WATER",
            "FRESH_NATURE",
            "ISF",
            "CUSTOM_COLOR",
        ],
        "maxSpeed": 255,
    },
}

AMBILIGHT_SUPPORTED_STYLES_EXTENDED_SAPHI: Dict[str, AmbilightSupportedStyleType] = {
    "FOLLOW_AUDIO": {
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
    "Lounge light": {
        "styleName": "Lounge light",
        "algorithms": ["MANUAL_HUE", "AUTOMATIC_HUE"],
        "maxSpeed": 255,
    },
}

AMBILIGHT_SUPPORTED_STYLES_EXTENDED = {
    "android": AMBILIGHT_SUPPORTED_STYLES_EXTENDED_ANDROID,
    "saphi": AMBILIGHT_SUPPORTED_STYLES_EXTENDED_SAPHI
}

AMBILIGHT_CURRENT_CONFIGURATION: AmbilightCurrentConfiguration = {
    "styleName": "FOLLOW_VIDEO",
    "isExpert": False,
    "menuSetting": "STANDARD",
    "stringValue": "Standard",
}

POWERSTATE = {"powerstate": "On"}
SCREENSTATE = {"screenstate": "On"}

CONTEXT: ContextType = {
    "data": "NA",
    "level1": "WatchTv",
    "level2": "Playstate",
    "level3": "NA",
}
