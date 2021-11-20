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
    MenuItemsSettingsCurrent,
    MenuItemsSettingsCurrentPost,
    MenuItemsSettingsNode,
    MenuItemsSettingsStructure,
    MenuItemsSettingsUpdate,
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

MENUITEMS_SETTINGS_STRUCTURE: MenuItemsSettingsStructure = {
  "node": {
    "node_id": 2131230753,
    "type": "PARENT_NODE",
    "string_id": "org.droidtv.ui.strings.R.string.MAIN_VB_SETUP",
    "context": "Setup_Menu",
    "data": {
      "nodes": [
        {
          "node_id": 2131230857,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_PICTURE",
          "context": "picture",
          "data": {
            "nodes": [
              {
                "node_id": 2131230858,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_PICTURE_STYLE",
                "context": "picture_style",
                "data": {
                  "enums": [
                    {
                      "enum_id": 23,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_AI"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PERSONAL"
                    },
                    {
                      "enum_id": 2,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIVID"
                    },
                    {
                      "enum_id": 3,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_NATURAL"
                    },
                    {
                      "enum_id": 4,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_STANDARD",
                      "icon": "org.droidtv.ui.tvwidget2k15.R.drawable.eco_16x12_146"
                    },
                    {
                      "enum_id": 5,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MOVIE"
                    },
                    {
                      "enum_id": 6,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAME"
                    },
                    {
                      "enum_id": 14,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MONITOR"
                    },
                    {
                      "enum_id": 24,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDR_AI"
                    },
                    {
                      "enum_id": 13,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_PERSONAL"
                    },
                    {
                      "enum_id": 9,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_VIVID"
                    },
                    {
                      "enum_id": 20,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_DOLBY_VISION_BRIGHT"
                    },
                    {
                      "enum_id": 21,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_DOLBY_VISION_DARK"
                    },
                    {
                      "enum_id": 10,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_NATURAL"
                    },
                    {
                      "enum_id": 11,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_MOVIE"
                    },
                    {
                      "enum_id": 12,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_GAME"
                    },
                    {
                      "enum_id": 7,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ISF_DAY",
                      "icon": "org.droidtv.ui.tvwidget2k15.R.drawable.isf_unlocked_d"
                    },
                    {
                      "enum_id": 8,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ISF_NIGHT",
                      "icon": "org.droidtv.ui.tvwidget2k15.R.drawable.isf_unlocked_d"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230859,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_COLOUR",
                "context": "colour",
                "data": {
                  "slider_data": {
                    "min": 0,
                    "max": 100,
                    "step_size": 1
                  }
                },
                "type": "SLIDER_NODE"
              },
              {
                "node_id": 2131230860,
                "context": "contrast",
                "data": {
                  "slider_data": {
                    "min": 0,
                    "max": 100,
                    "step_size": 1
                  }
                },
                "type": "SLIDER_NODE"
              },
              {
                "node_id": 2131230861,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_SHARPNESS",
                "context": "sharpness",
                "data": {
                  "slider_data": {
                    "min": 0,
                    "max": 10,
                    "step_size": 1
                  }
                },
                "type": "SLIDER_NODE"
              },
              {
                "node_id": 2131230862,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_BRIGHTNESS",
                "context": "brightness",
                "data": {
                  "slider_data": {
                    "min": 0,
                    "max": 100,
                    "step_size": 1
                  }
                },
                "type": "SLIDER_NODE"
              },
              {
                "node_id": 2131230863,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_ADVANCED_PICTURE",
                "context": "advanced_picture",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230864,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_COLOUR",
                      "context": "colour_menu",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230865,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TINT_HUE",
                            "context": "tint",
                            "data": {
                              "slider_data": {
                                "min": -50,
                                "max": 50,
                                "step_size": 1
                              }
                            },
                            "type": "SLIDER_NODE"
                          },
                          {
                            "node_id": 2131230866,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_COLOUR_ENHANCEMENT",
                            "context": "colour_enhancement",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230867,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_COLOUR_GAMUT",
                            "context": "colour_gamut",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORMAL"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_WIDE"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230868,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_COLOUR_TEMPERATURE",
                            "context": "colour_temperature",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORMAL"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_WARM"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_COOL"
                                },
                                {
                                  "enum_id": 4,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_CUSTOM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230869,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WHITEPOINT_ALIGNMENT",
                            "context": "whitepoint_alignment_item",
                            "data": {
                              "sliders": [
                                {
                                  "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_RED_WP",
                                  "slider_data": {
                                    "min": 0,
                                    "max": 127,
                                    "step_size": 1
                                  }
                                },
                                {
                                  "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_GREEN_WP",
                                  "slider_data": {
                                    "min": 0,
                                    "max": 127,
                                    "step_size": 1
                                  }
                                },
                                {
                                  "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_BLUE_WP",
                                  "slider_data": {
                                    "min": 0,
                                    "max": 127,
                                    "step_size": 1
                                  }
                                },
                                {
                                  "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_RED_BL",
                                  "slider_data": {
                                    "min": -7,
                                    "max": 8,
                                    "step_size": 1
                                  }
                                },
                                {
                                  "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_GREEN_BL",
                                  "slider_data": {
                                    "min": -7,
                                    "max": 8,
                                    "step_size": 1
                                  }
                                },
                                {
                                  "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_BLUE_BL",
                                  "slider_data": {
                                    "min": -7,
                                    "max": 8,
                                    "step_size": 1
                                  }
                                }
                              ]
                            },
                            "type": "MULTIPLE_SLIDER"
                          },
                          {
                            "node_id": 2131230870,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WHITEPOINT_ALIGNMENT",
                            "context": "whitepoint_alignment_menu",
                            "data": {
                              "nodes": [
                                {
                                  "node_id": 2131230871,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_WHITEPOINT_ALIGNMENT_2POINT",
                                  "context": "whitepoint_alignment",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_RED_WP",
                                        "slider_data": {
                                          "min": 0,
                                          "max": 127,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_GREEN_WP",
                                        "slider_data": {
                                          "min": 0,
                                          "max": 127,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_BLUE_WP",
                                        "slider_data": {
                                          "min": 0,
                                          "max": 127,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_RED_BL",
                                        "slider_data": {
                                          "min": -7,
                                          "max": 8,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_GREEN_BL",
                                        "slider_data": {
                                          "min": -7,
                                          "max": 8,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_BLUE_BL",
                                        "slider_data": {
                                          "min": -7,
                                          "max": 8,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                },
                                {
                                  "node_id": 2131230872,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_WHITEPOINT_ALIGNMENT_20POINT",
                                  "context": "whitepoint_alignment",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_LEVEL",
                                        "slider_data": {
                                          "min": 1,
                                          "max": 20,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_RED_OFFSET",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_GREEN_OFFSET",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_BLUE_OFFSET",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                }
                              ]
                            }
                          },
                          {
                            "node_id": 2131230873,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_COLOUR_CONTROL",
                            "context": "colour_control",
                            "data": {
                              "nodes": [
                                {
                                  "node_id": 2131230874,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MS_RED",
                                  "context": "colour_control",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_HUE",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_SATURATION",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_INTENSITY",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                },
                                {
                                  "node_id": 2131230875,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MS_YELLOW",
                                  "context": "colour_control",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_HUE",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_SATURATION",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_INTENSITY",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                },
                                {
                                  "node_id": 2131230876,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MS_GREEN",
                                  "context": "colour_control",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_HUE",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_SATURATION",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_INTENSITY",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                },
                                {
                                  "node_id": 2131230877,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MS_CYAN",
                                  "context": "colour_control",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_HUE",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_SATURATION",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_INTENSITY",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                },
                                {
                                  "node_id": 2131230878,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MS_BLUE",
                                  "context": "colour_control",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_HUE",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_SATURATION",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_INTENSITY",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                },
                                {
                                  "node_id": 2131230879,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MS_MAGENTA",
                                  "context": "colour_control",
                                  "data": {
                                    "sliders": [
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_HUE",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_SATURATION",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      },
                                      {
                                        "slider_id": "org.droidtv.ui.strings.R.string.MAIN_INTENSITY",
                                        "slider_data": {
                                          "min": -15,
                                          "max": 15,
                                          "step_size": 1
                                        }
                                      }
                                    ]
                                  },
                                  "type": "MULTIPLE_SLIDER"
                                },
                                {
                                  "node_id": 2131230880,
                                  "type": "PARENT_NODE",
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_RESET_ALL",
                                  "context": "reset_all",
                                  "data": {}
                                }
                              ]
                            }
                          },
                          {
                            "node_id": 2131230881,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_RGB_ONLY_MODE",
                            "context": "rgb_only_mode",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_RED"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_GREEN"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_BLUE"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230882,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CONTRAST_MENU",
                      "context": "contrast_menu",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230883,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CONTRAST_MODE",
                            "context": "contrast_modes",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORMAL"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OPTMIZED_FOR_PICTURE"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OPTMIZED_FOR_ENERGY_SAVING"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230884,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDR_UPSCALING",
                            "context": "hdr_upscaling",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230885,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PNR",
                            "context": "perfect_natural_reality",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230886,
                            "context": "hd_ultra_hdr",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                },
                                {
                                  "enum_id": 4,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUTO_3D_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230887,
                            "context": "perfect_contrast",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230888,
                            "context": "video_contrast",
                            "data": {
                              "slider_data": {
                                "min": 0,
                                "max": 100,
                                "step_size": 1
                              }
                            },
                            "type": "SLIDER_NODE"
                          },
                          {
                            "node_id": 2131230889,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LIGHT_SENSOR",
                            "context": "light_sensor",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230890,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAMMA",
                            "context": "gamma",
                            "data": {
                              "slider_data": {
                                "min": -4,
                                "max": 4,
                                "step_size": 1
                              }
                            },
                            "type": "SLIDER_NODE"
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230891,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SHARPNESS",
                      "context": "sharpness_menu",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230892,
                            "context": "super_resolution",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230893,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PICTURE_CLEAN",
                      "context": "picture_clean_menu",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230894,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NOISE_REDUCTION",
                            "context": "noise_reduction",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230895,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MPEG_ARTEFACT_REDUCTION",
                            "context": "mpeg_artefact_reduction",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230896,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MOTION_MENU",
                      "context": "motion_menu",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230897,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MOTION_STYLE",
                            "context": "motion_style",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_PURE_CINEMA"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MOVIE"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_STANDARD"
                                },
                                {
                                  "enum_id": 4,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_SMOOTH"
                                },
                                {
                                  "enum_id": 5,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_PERSONAL"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230898,
                            "context": "hd_natural_motion",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230899,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_PERFECT_CLEAN_MOTION",
                            "context": "clear_lcd",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          }
                        ]
                      }
                    }
                  ]
                }
              },
              {
                "node_id": 2131230900,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_ADVANCED_PICTURE_AI_SETTINGS",
                "context": "advanced_ai_settings",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230901,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PERFECT_CONTRAST_AI",
                      "context": "advanced_ai_settings",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230902,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PERFECT_COLOUR_AI",
                      "context": "advanced_ai_settings",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230903,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PERFECT_SHARPNESS_AI",
                      "context": "advanced_ai_settings",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230904,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SOURCE_PERFECTION_AI",
                      "context": "advanced_ai_settings",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230905,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PERFECT_MOTION_AI",
                      "context": "advanced_ai_settings",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230906,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_PICTURE_FORMAT",
                "context": "picture_format",
                "data": {}
              },
              {
                "node_id": 2131230907,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_DOLBY_VISION_NOTIFICATION",
                "context": "dolby_vision_notification",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230908,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_QUICK_PICTURE_SETTINGS",
                "context": "quick_picture_settings",
                "data": {}
              }
            ]
          }
        },
        {
          "node_id": 2131230910,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_SOUND",
          "context": "sound",
          "data": {
            "nodes": [
              {
                "node_id": 2131230911,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_SOUND_STYLE",
                "context": "sound_style",
                "data": {
                  "enums": []
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230912,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_SOUND_STYLE",
                "context": "sound_style",
                "data": {
                  "enums": []
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230913,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEADPHONE_VOLUME",
                "context": "headphones_volume",
                "data": {
                  "slider_data": {
                    "min": 0,
                    "max": 60,
                    "step_size": 1
                  }
                },
                "type": "SLIDER_NODE"
              },
              {
                "node_id": 2131230914,
                "type": "PARENT_NODE",
                "context": "sound_expert_mode",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230915,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPEAKER_VIRTUALIZER",
                      "context": "personal_dolby_atmos",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DOLBY_ATMOS_AUTO"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230916,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_CLEAR_DIALOGUE",
                      "context": "clear_dialogue",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230917,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AI_EQUALIZER",
                      "context": "expert_equalizer",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230918,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CUSTOM_AI_EQUALIZER",
                      "context": "expert_equalizer",
                      "data": {
                        "sliders": [
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MISC_100_HZ",
                            "slider_data": {
                              "min": -8,
                              "max": 8,
                              "step_size": 1
                            }
                          },
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MISC_300_HZ",
                            "slider_data": {
                              "min": -8,
                              "max": 8,
                              "step_size": 1
                            }
                          },
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MISC_1_KHZ",
                            "slider_data": {
                              "min": -8,
                              "max": 8,
                              "step_size": 1
                            }
                          },
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MISC_3_KHZ",
                            "slider_data": {
                              "min": -8,
                              "max": 8,
                              "step_size": 1
                            }
                          },
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MISC_10_KHZ",
                            "slider_data": {
                              "min": -8,
                              "max": 8,
                              "step_size": 1
                            }
                          }
                        ]
                      },
                      "type": "MULTIPLE_SLIDER"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230919,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_TV_POSITION",
                "context": "tv_placement",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_WALL_MOUNTED"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON_TV_STAND"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230920,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_DTS_PLAY_FI",
                "context": "DTS_Play_Fi",
                "data": {}
              },
              {
                "node_id": 2131230921,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_ADVANCED_SOUND",
                "context": "advanced_sound",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230922,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUTO_VOLUME",
                      "context": "auto_volume_leveling",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NIGHT_MODE"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230923,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_DELTA_VOLUME",
                      "context": "DeltaVolume",
                      "data": {
                        "slider_data": {
                          "min": -12,
                          "max": 12,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230924,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUDIO_OUT",
                      "context": "tv_speakers",
                      "data": {
                        "enums": []
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230925,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_DIGITAL_OUTPUT_FORMAT",
                      "context": "digital_output_format",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MULTICHANNEL"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.SPDIF_OUTPUT_3"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PCM"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230926,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_DIGITAL_OUTPUT_LEVEL",
                      "context": "digital_output_level",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPDIF_MORE"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPDIF_MEDIUM"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPDIF_LESS"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230927,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUDIO_OUT_DELAY",
                      "context": "audio_out_delay",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NO_LATENCY"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IN_LIPSYNC"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230928,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUDIO_OUT_OFFSET",
                      "context": "audio_out_offset",
                      "data": {
                        "slider_data": {
                          "min": 0,
                          "max": 60,
                          "step_size": 5
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230929,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SUBWOOFER_OUT",
                      "context": "subwoofer_out",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230930,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CENTRE_SPEAKER_VOLUME",
                      "context": "centre_speaker_volume",
                      "data": {
                        "slider_data": {
                          "min": -3,
                          "max": 3,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230931,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEIGHT_SPEAKER_VOLUME",
                      "context": "height_speaker_volume",
                      "data": {
                        "slider_data": {
                          "min": -3,
                          "max": 3,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230932,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_DOLBY_ATMOS_NOTIFICATION",
                "context": "dolby_atmos_notification",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                    }
                  ]
                },
                "type": "LIST_NODE"
              }
            ]
          }
        },
        {
          "node_id": 2131230765,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MISC_AMBILIGHT",
          "context": "ambilight",
          "data": {
            "nodes": [
              {
                "node_id": 2131230766,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_STYLE",
                "context": "ambilight_style",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230767,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_STYLE_OFF",
                      "context": "ambilight_off",
                      "data": {}
                    },
                    {
                      "node_id": 2131230768,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_FOLLOW_VIDEO",
                      "context": "ambilight_follow_video",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_STANDARD"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_NATURAL"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_SPORTS"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_VIVID"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_GAME"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230769,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_FOLLOW_AUDIO",
                      "context": "ambilight_follow_audio",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 101,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FOLLOW_AUDIO_STYLE_1"
                          },
                          {
                            "enum_id": 103,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FOLLOW_AUDIO_STYLE_3"
                          },
                          {
                            "enum_id": 107,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FOLLOW_AUDIO_STYLE_6"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230770,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_FOLLOW_COLOUR_2K20",
                      "context": "ambilight_lounge_light",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 201,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOUNGE_LIGHT_MODE_2"
                          },
                          {
                            "enum_id": 202,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOUNGE_LIGHT_MODE_3"
                          },
                          {
                            "enum_id": 203,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOUNGE_LIGHT_MODE_1"
                          },
                          {
                            "enum_id": 207,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WARM_WHITE"
                          },
                          {
                            "enum_id": 208,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CUSTOM_COLOUR"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230771,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_FOLLOW_FLAG",
                      "context": "ambilight_follow_flag",
                      "data": {}
                    },
                    {
                      "node_id": 2131230772,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_FOLLOW_APP",
                      "context": "ambilight_follow_app",
                      "data": {}
                    }
                  ]
                }
              },
              {
                "node_id": 2131230773,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_CUSTOM_COLOUR",
                "context": "ambilight_custom_colour",
                "data": {
                  "colors": [
                    -14411265,
                    -15097089,
                    -15074561,
                    -15073484,
                    -1442023,
                    -19943,
                    -59111,
                    -58908,
                    -11647489,
                    -12208897,
                    -12190721,
                    -12189861,
                    -1179835,
                    -16059,
                    -47803,
                    -47639,
                    -8883713,
                    -9320705,
                    -9306881,
                    -9306238,
                    -917647,
                    -12175,
                    -36495,
                    -36370,
                    -6119937,
                    -6432769,
                    -6423041,
                    -6422615,
                    -589923,
                    -8547,
                    -25187,
                    -25101,
                    -3356161,
                    -3544577,
                    -3539201,
                    -3538993,
                    -327735,
                    -4663,
                    -13879,
                    -13831,
                    -2323,
                    -1807,
                    -1035,
                    -520,
                    -4,
                    -67329,
                    -461313,
                    -789761
                  ]
                },
                "type": "COLOR_PICKER_NODE"
              },
              {
                "node_id": 2131230774,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP",
                "context": "ambisleep",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230775,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_ON",
                      "context": "ambisleep_on",
                      "data": {}
                    },
                    {
                      "node_id": 2131230776,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_DURATION",
                      "context": "ambisleep_duration",
                      "data": {
                        "slider_data": {
                          "min": 1,
                          "max": 60,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230777,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_BRIGHTNESS",
                      "context": "ambisleep_brightness",
                      "data": {
                        "slider_data": {
                          "min": 1,
                          "max": 9,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230778,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_COLOUR",
                      "context": "ambisleep_colour",
                      "data": {
                        "colors": [
                          -62976,
                          -45056,
                          -37376,
                          -29696,
                          -14336
                        ]
                      },
                      "type": "COLOR_PICKER_NODE"
                    },
                    {
                      "node_id": 2131230779,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND",
                      "context": "ambisleep_sound",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_CAMPFIRE"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_HOWLING_WIND"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_RAIN"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_RAINFOREST"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_SUMMER_NIGHT"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_TROPICAL_BEACH"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_WATERFALL"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBISLEEP_SOUND_NO_SOUND"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230780,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_EXTENSION",
                "context": "ambilight_extension",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230781,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_PLUS_HUE",
                      "context": "ambilight_hue_menu",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230782,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_HUE_CONFIGURE",
                            "context": "ambilight_hue_wizard",
                            "data": {}
                          },
                          {
                            "node_id": 2131230783,
                            "context": "ambilight_hue_off",
                            "data": {},
                            "type": "TOGGLE_NODE"
                          },
                          {
                            "node_id": 2131230784,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_HUE_FOLLOW_AMBILIGHT",
                            "context": "ambilight_hue_follow_ambilight",
                            "data": {
                              "slider_data": {
                                "min": 0,
                                "max": 10,
                                "step_size": 1
                              }
                            },
                            "type": "SLIDER_NODE"
                          },
                          {
                            "node_id": 2131230785,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOUNGE_LIGHT_HUE",
                            "context": "ambilight_lounge_light_hue",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230786,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_HUE_STATUS",
                            "context": "ambilight_hue_status",
                            "data": {}
                          },
                          {
                            "node_id": 2131230787,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_HUE_RESET",
                            "context": "ambilight_hue_reset_configuration",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230788,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_AIR",
                      "context": "ambilight_light_play",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230789,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_AIR_CONFIGURE",
                            "context": "ambilight_light_play",
                            "data": {}
                          },
                          {
                            "node_id": 2131230790,
                            "type": "PARENT_NODE",
                            "context": "ambilight_light_play",
                            "data": {}
                          },
                          {
                            "node_id": 2131230791,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOUNGE_LIGHT_AIR",
                            "context": "ambilight_light_play",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOUNGE_LIGHT_AIR_LABEL_1"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOUNGE_LIGHT_AIR_LABEL_2"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230792,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_AIR_STATUS",
                            "context": "ambilight_light_play",
                            "data": {}
                          },
                          {
                            "node_id": 2131230793,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_AIR_RESET",
                            "context": "ambilight_light_play",
                            "data": {}
                          }
                        ]
                      }
                    }
                  ]
                }
              },
              {
                "node_id": 2131230794,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_ADVANCED_AMBILIGHT",
                "context": "ambilight_advanced",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230795,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_BRIGHTNESS",
                      "context": "ambilight_brightness",
                      "data": {
                        "slider_data": {
                          "min": 0,
                          "max": 10,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230796,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_SATURATION",
                      "context": "ambilight_saturation",
                      "data": {
                        "slider_data": {
                          "min": -2,
                          "max": 2,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230797,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AMBILIGHT_BOTTOM_SIDE",
                      "context": "ambilight_bottom_side",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230798,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_BRIGHTNESS_BOTTOM_SIDE",
                      "context": "ambilight_brightness_bottom_side",
                      "data": {
                        "slider_data": {
                          "min": 0,
                          "max": 10,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230799,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_WALL_COLOUR",
                      "context": "ambilight_wall_colour",
                      "data": {
                        "colors": [
                          -1,
                          -1651276,
                          -3342439,
                          -3347201,
                          -3355393,
                          -13108,
                          -6451,
                          -103,
                          -12566464,
                          -3693173,
                          -6565376,
                          -10053121,
                          -2982751,
                          -33664,
                          -81560,
                          -256,
                          -15724528,
                          -7508135,
                          -10452480,
                          -15513423,
                          -5293203,
                          -1888983,
                          -5682169,
                          -26368
                        ]
                      },
                      "type": "WALL_COLOR_NODE"
                    },
                    {
                      "node_id": 2131230800,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TV_SWITCH_OFF",
                      "context": "ambilight_tv_switch_off",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FADE_OUT"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IMMEDIATE_SWITCH_OFF"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230801,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ISF_TUNING",
                      "context": "ambilight_isf_tuning",
                      "data": {
                        "sliders": [
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_RED",
                            "slider_data": {
                              "min": 0,
                              "max": 100,
                              "step_size": 1
                            }
                          },
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_GREEN",
                            "slider_data": {
                              "min": 0,
                              "max": 100,
                              "step_size": 1
                            }
                          },
                          {
                            "slider_id": "org.droidtv.ui.strings.R.string.MAIN_MS_BLUE",
                            "slider_data": {
                              "min": 0,
                              "max": 100,
                              "step_size": 1
                            }
                          }
                        ]
                      },
                      "type": "MULTIPLE_SLIDER"
                    }
                  ]
                }
              }
            ]
          }
        },
        {
          "node_id": 2131230829,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_ECO_SETTINGS",
          "context": "eco_settings",
          "data": {
            "nodes": [
              {
                "node_id": 2131230830,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_ENERGY_SAVING",
                "context": "energy_saving",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                    },
                    {
                      "enum_id": 2,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                    },
                    {
                      "enum_id": 3,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230831,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_MUTE_SCREEN",
                "context": "screen_off",
                "data": {}
              },
              {
                "node_id": 2131230832,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_LIGHT_SENSOR",
                "context": "eco_settings_light_sensor",
                "data": {}
              },
              {
                "node_id": 2131230833,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUTOMATIC_SWITCH_OFF",
                "context": "switch_off_timer",
                "data": {
                  "slider_data": {
                    "min": 0,
                    "max": 240,
                    "step_size": 30
                  }
                },
                "type": "SLIDER_NODE"
              }
            ]
          }
        },
        {
          "node_id": 2131230938,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_GENERAL_SETTINGS",
          "context": "general_settings",
          "data": {
            "nodes": [
              {
                "node_id": 2131230939,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_USB_STORAGE",
                "context": "usb_storage",
                "data": {}
              },
              {
                "node_id": 2131230940,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_USB_KEYBOARD_SETTINGS",
                "context": "usb_keyboard_settings",
                "data": {}
              },
              {
                "node_id": 2131230941,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_PHILIPS_WORDMARK",
                "context": "philips_wordmark",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MINIMUM"
                    },
                    {
                      "enum_id": 2,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MEDIUM"
                    },
                    {
                      "enum_id": 3,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAXIMUM"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230942,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOCATION",
                "context": "location",
                "data": {
                  "enums": [
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HOME"
                    },
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SHOP"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230943,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_VB_SHOP_CONFIGURATION",
                "context": "shop_setup",
                "data": {}
              },
              {
                "node_id": 2131230944,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MISC_EASYLINK",
                "context": "easylink_menu",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230945,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_EASYLINK",
                      "context": "easylink",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230946,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_EASYLINK_REMOTE_CONTROL",
                      "context": "easylink_remote_control",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230947,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_SETTINGS",
                "context": "pdel",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230948,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_ENABLE_ON_STANDBY",
                      "context": "pdel",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230949,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_BRIGHTNESS",
                      "context": "pdel",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_BRIGHTNESS_LOW"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_BRIGHTNESS_MEDIUM"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_BRIGHTNESS_HIGH"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_BRIGHTNESS_MAXIMUM"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230950,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_DURATION",
                      "context": "pdel",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_DURATION_10_MINUTE"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_DURATION_20_MINUTE"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_DURATION_30_MINUTE"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_DURATION_40_MINUTE"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_DURATION_50_MINUTE"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PD_EXPERIENCE_LIGHT_DURATION_60_MINUTE"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230951,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI_ULTRA_HD",
                "context": "hdmi_ultra_hd",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230952,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI1",
                      "context": "hdmi_ultra_hd",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_STANDARD_2K18"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_OPTIMAL_2K18"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230953,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI2",
                      "context": "hdmi_ultra_hd",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_STANDARD_2K18"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_OPTIMAL_2K18"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230954,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI3",
                      "context": "hdmi_ultra_hd",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_STANDARD_2K18"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_OPTIMAL_2K18"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230955,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI4",
                      "context": "hdmi_ultra_hd",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_STANDARD_2K18"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UHD_OPTIMAL_2K18"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230956,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDMI_AUTO_GAME_MODE",
                "context": "hdmi_auto_game_mode",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230957,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI1",
                      "context": "hdmi_auto_game_mode",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230958,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI2",
                      "context": "hdmi_auto_game_mode",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230959,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI3",
                      "context": "hdmi_auto_game_mode",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230960,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_HDMI4",
                      "context": "hdmi_auto_game_mode",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230961,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_HDMI_AUTO_MOVIE_MODE",
                "context": "auto_movie_mode",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230962,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_ADVANCED_INSTALLATION",
                "context": "advanced_general_settings",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230963,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_HBBTV_SETTINGS",
                      "context": "hbbtv_settings",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230964,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_HBB_TV",
                            "context": "hbbtv",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230965,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HBBTV_TRACK_USAGE",
                            "context": "hbbtv_track_usage",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230966,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HBBTV_COOKIES",
                            "context": "hbbtv_cookies",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 0,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230967,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CLEAR_APPROVED_APP_LISTING",
                            "context": "hbbtv_clear_listing",
                            "data": {}
                          },
                          {
                            "node_id": 2131230968,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HBBTV_DEVICEID_RESET",
                            "context": "hbbtv_device_id_reset",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230969,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OLED_SCREEN_SETTINGS",
                      "context": "OLED_screen_settings",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230970,
                            "context": "still_image_protection",
                            "data": {
                              "enums": [
                                {
                                  "enum_id": 1,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                                },
                                {
                                  "enum_id": 2,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORMAL"
                                },
                                {
                                  "enum_id": 3,
                                  "string_id": "org.droidtv.ui.strings.R.string.MAIN_HIGH"
                                }
                              ]
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 2131230909,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CLEAR_IMAGE_RESIDUAL",
                            "context": "clear_image_residual",
                            "data": {}
                          }
                        ]
                      }
                    }
                  ]
                }
              },
              {
                "node_id": 2131230971,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIEWING_DATA",
                "context": "viewing_data",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230972,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIEWING_DATA_SETTINGS",
                      "context": "viewing_data_settings",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230973,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PRIVACY_POLICY",
                      "context": "privacy_policy",
                      "data": {}
                    }
                  ]
                }
              },
              {
                "node_id": 2131230974,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_FACTORY_SETTINGS",
                "context": "factory_settings",
                "data": {}
              },
              {
                "node_id": 2131230975,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_REINSTALL_TV",
                "context": "reinstall_tv",
                "data": {}
              },
              {
                "node_id": 2131230976,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.CAM_PROFILE_NAME",
                "context": "CAM_profile_name",
                "data": {}
              }
            ]
          }
        },
        {
          "node_id": 2131230834,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_REGION_AND_LANGUAGE",
          "context": "region_languages",
          "data": {
            "nodes": [
              {
                "node_id": 2131230835,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_LANGUAGES",
                "context": "languages",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230836,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MENU_LANGUAGE",
                      "context": "menu_language",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 83,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_AZERBAIJANI"
                          },
                          {
                            "enum_id": 48,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_BAHASA_MELAYU"
                          },
                          {
                            "enum_id": 50,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_INDONESIAN"
                          },
                          {
                            "enum_id": 37,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_BULGARIAN"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_CZECH"
                          },
                          {
                            "enum_id": 14,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_DANISH"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_GERMAN"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ENGLISH"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_SPANISH"
                          },
                          {
                            "enum_id": 26,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ESTONIAN"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_GREEK"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_FRENCH"
                          },
                          {
                            "enum_id": 43,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_IRISH"
                          },
                          {
                            "enum_id": 13,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_CROATIAN"
                          },
                          {
                            "enum_id": 75,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ICELANDIC"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ITALIAN"
                          },
                          {
                            "enum_id": 41,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_KAZAKH"
                          },
                          {
                            "enum_id": 40,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_LATVIAN"
                          },
                          {
                            "enum_id": 39,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_LITHUANIAN"
                          },
                          {
                            "enum_id": 52,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_MACEDONIAN"
                          },
                          {
                            "enum_id": 30,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_HUNGARIAN"
                          },
                          {
                            "enum_id": 78,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_MONGOLIAN"
                          },
                          {
                            "enum_id": 15,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_DUTCH"
                          },
                          {
                            "enum_id": 19,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_NORWEGIAN"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_POLISH"
                          },
                          {
                            "enum_id": 20,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_PORTUGUESE"
                          },
                          {
                            "enum_id": 36,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_PORTUGUESE_BRAZILIAN"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_RUSSIAN"
                          },
                          {
                            "enum_id": 25,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ROMANIAN"
                          },
                          {
                            "enum_id": 74,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ALBANIAN"
                          },
                          {
                            "enum_id": 21,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_SERBIAN"
                          },
                          {
                            "enum_id": 22,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_SLOVAK"
                          },
                          {
                            "enum_id": 23,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_SLOVENIAN"
                          },
                          {
                            "enum_id": 16,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_FINNISH"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_SWEDISH"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_TURKISH"
                          },
                          {
                            "enum_id": 51,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_VIETNAMESE"
                          },
                          {
                            "enum_id": 27,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_UKRAINIAN"
                          },
                          {
                            "enum_id": 49,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_TRADITIONAL_CHINESE"
                          },
                          {
                            "enum_id": 34,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_CHINESE"
                          },
                          {
                            "enum_id": 28,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ARABIC"
                          },
                          {
                            "enum_id": 29,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_HEBREW"
                          },
                          {
                            "enum_id": 45,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_THAI"
                          },
                          {
                            "enum_id": 58,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_HINDI"
                          },
                          {
                            "enum_id": 79,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_BENGALI"
                          },
                          {
                            "enum_id": 80,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_TELUGU"
                          },
                          {
                            "enum_id": 81,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_MARATHI"
                          },
                          {
                            "enum_id": 53,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_TAMIL"
                          },
                          {
                            "enum_id": 82,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_ARMENIAN"
                          },
                          {
                            "enum_id": 84,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_GEORGIAN"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230837,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PRIMARY_AUDIO",
                      "context": "primary_audio",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 74,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALBANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 85,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALTERNATIVE_LANGUAGE_A"
                          },
                          {
                            "enum_id": 86,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALTERNATIVE_LANGUAGE_B"
                          },
                          {
                            "enum_id": 28,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARABIC_TRANSLATED"
                          },
                          {
                            "enum_id": 82,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARMENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 83,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AZERBAIJANI_TRANSLATED"
                          },
                          {
                            "enum_id": 48,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BAHASA_MELAYU_TRANSLATED"
                          },
                          {
                            "enum_id": 11,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BASQUE_TRANSLATED"
                          },
                          {
                            "enum_id": 37,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BULGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 12,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CATALAN_TRANSLATED"
                          },
                          {
                            "enum_id": 49,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 61,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MANDARIN_TRANSLATED"
                          },
                          {
                            "enum_id": 76,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CANTONESE_TRANSLATED"
                          },
                          {
                            "enum_id": 13,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CROATIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CZECH_TRANSLATED"
                          },
                          {
                            "enum_id": 14,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 15,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DUTCH_TRANSLATED"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ENGLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 26,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ESTONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 16,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FINNISH_TRANSLATED"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FRENCH_TRANSLATED"
                          },
                          {
                            "enum_id": 18,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GALLEGAN_TRANSLATED"
                          },
                          {
                            "enum_id": 84,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GEORGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GERMAN_TRANSLATED"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GREEK_TRANSLATED"
                          },
                          {
                            "enum_id": 29,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEBREW_TRANSLATED"
                          },
                          {
                            "enum_id": 58,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HINDI_TRANSLATED"
                          },
                          {
                            "enum_id": 30,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HUNGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 46,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_AUDIO"
                          },
                          {
                            "enum_id": 59,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECOND_AUDIO"
                          },
                          {
                            "enum_id": 60,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THIRD_AUDIO"
                          },
                          {
                            "enum_id": 47,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MULTIPLE_LANGUAGES"
                          },
                          {
                            "enum_id": 75,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ICELANDIC_TRANSLATED"
                          },
                          {
                            "enum_id": 50,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 43,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IRISH_TRANSLATED"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ITALIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 57,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_JAPANESE_TRANSLATED"
                          },
                          {
                            "enum_id": 41,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_TRANSLATED"
                          },
                          {
                            "enum_id": 55,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KOREAN_TRANSLATED"
                          },
                          {
                            "enum_id": 40,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LATVIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 39,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LITHUANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 52,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MACEDONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 54,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAORI_TRANSLATED"
                          },
                          {
                            "enum_id": 19,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORWEGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 44,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_LANGUAGE"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_POLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 20,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PORTUGUESE_TRANSLATED"
                          },
                          {
                            "enum_id": 25,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ROMANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_RUSSIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 72,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SAMI_TRANSLATED"
                          },
                          {
                            "enum_id": 17,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAELIC_TRANSLATED"
                          },
                          {
                            "enum_id": 34,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SIMPLIFIED_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 22,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVAK_TRANSLATED"
                          },
                          {
                            "enum_id": 23,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 21,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SERBIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWEDISH_TRANSLATED"
                          },
                          {
                            "enum_id": 53,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TAMIL_TRANSLATED"
                          },
                          {
                            "enum_id": 45,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THAI_TRANSLATED"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TURKISH_TRANSLATED"
                          },
                          {
                            "enum_id": 27,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UKRAINIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 51,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIETNAMESE_TRANSLATED"
                          },
                          {
                            "enum_id": 24,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WELSH_TRANSLATED"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230838,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECONDARY_AUDIO",
                      "context": "secondary_audio",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 74,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALBANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 85,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALTERNATIVE_LANGUAGE_A"
                          },
                          {
                            "enum_id": 86,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALTERNATIVE_LANGUAGE_B"
                          },
                          {
                            "enum_id": 28,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARABIC_TRANSLATED"
                          },
                          {
                            "enum_id": 82,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARMENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 83,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AZERBAIJANI_TRANSLATED"
                          },
                          {
                            "enum_id": 48,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BAHASA_MELAYU_TRANSLATED"
                          },
                          {
                            "enum_id": 11,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BASQUE_TRANSLATED"
                          },
                          {
                            "enum_id": 37,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BULGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 12,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CATALAN_TRANSLATED"
                          },
                          {
                            "enum_id": 49,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 61,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MANDARIN_TRANSLATED"
                          },
                          {
                            "enum_id": 76,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CANTONESE_TRANSLATED"
                          },
                          {
                            "enum_id": 13,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CROATIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CZECH_TRANSLATED"
                          },
                          {
                            "enum_id": 14,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 15,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DUTCH_TRANSLATED"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ENGLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 26,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ESTONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 16,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FINNISH_TRANSLATED"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FRENCH_TRANSLATED"
                          },
                          {
                            "enum_id": 18,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GALLEGAN_TRANSLATED"
                          },
                          {
                            "enum_id": 84,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GEORGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GERMAN_TRANSLATED"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GREEK_TRANSLATED"
                          },
                          {
                            "enum_id": 29,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEBREW_TRANSLATED"
                          },
                          {
                            "enum_id": 58,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HINDI_TRANSLATED"
                          },
                          {
                            "enum_id": 30,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HUNGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 46,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_AUDIO"
                          },
                          {
                            "enum_id": 59,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECOND_AUDIO"
                          },
                          {
                            "enum_id": 60,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THIRD_AUDIO"
                          },
                          {
                            "enum_id": 47,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MULTIPLE_LANGUAGES"
                          },
                          {
                            "enum_id": 75,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ICELANDIC_TRANSLATED"
                          },
                          {
                            "enum_id": 50,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 43,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IRISH_TRANSLATED"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ITALIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 57,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_JAPANESE_TRANSLATED"
                          },
                          {
                            "enum_id": 41,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_TRANSLATED"
                          },
                          {
                            "enum_id": 55,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KOREAN_TRANSLATED"
                          },
                          {
                            "enum_id": 40,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LATVIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 39,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LITHUANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 52,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MACEDONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 54,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAORI_TRANSLATED"
                          },
                          {
                            "enum_id": 19,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORWEGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 44,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_LANGUAGE"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_POLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 20,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PORTUGUESE_TRANSLATED"
                          },
                          {
                            "enum_id": 25,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ROMANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_RUSSIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 72,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SAMI_TRANSLATED"
                          },
                          {
                            "enum_id": 17,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAELIC_TRANSLATED"
                          },
                          {
                            "enum_id": 34,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SIMPLIFIED_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 22,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVAK_TRANSLATED"
                          },
                          {
                            "enum_id": 23,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 21,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SERBIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWEDISH_TRANSLATED"
                          },
                          {
                            "enum_id": 53,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TAMIL_TRANSLATED"
                          },
                          {
                            "enum_id": 45,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THAI_TRANSLATED"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TURKISH_TRANSLATED"
                          },
                          {
                            "enum_id": 27,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UKRAINIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 51,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIETNAMESE_TRANSLATED"
                          },
                          {
                            "enum_id": 24,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WELSH_TRANSLATED"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230839,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PRIMARY_SUBTITLES",
                      "context": "primary_subtitles",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 74,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALBANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 28,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARABIC_TRANSLATED"
                          },
                          {
                            "enum_id": 82,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARMENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 83,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AZERBAIJANI_TRANSLATED"
                          },
                          {
                            "enum_id": 48,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BAHASA_MELAYU_TRANSLATED"
                          },
                          {
                            "enum_id": 11,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BASQUE_TRANSLATED"
                          },
                          {
                            "enum_id": 37,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BULGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 12,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CATALAN_TRANSLATED"
                          },
                          {
                            "enum_id": 49,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 61,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MANDARIN_TRANSLATED"
                          },
                          {
                            "enum_id": 76,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CANTONESE_TRANSLATED"
                          },
                          {
                            "enum_id": 13,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CROATIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CZECH_TRANSLATED"
                          },
                          {
                            "enum_id": 14,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 15,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DUTCH_TRANSLATED"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ENGLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 26,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ESTONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 16,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FINNISH_TRANSLATED"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FRENCH_TRANSLATED"
                          },
                          {
                            "enum_id": 18,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GALLEGAN_TRANSLATED"
                          },
                          {
                            "enum_id": 84,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GEORGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GERMAN_TRANSLATED"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GREEK_TRANSLATED"
                          },
                          {
                            "enum_id": 29,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEBREW_TRANSLATED"
                          },
                          {
                            "enum_id": 58,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HINDI_TRANSLATED"
                          },
                          {
                            "enum_id": 30,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HUNGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 46,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_AUDIO"
                          },
                          {
                            "enum_id": 59,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECOND_AUDIO"
                          },
                          {
                            "enum_id": 60,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THIRD_AUDIO"
                          },
                          {
                            "enum_id": 47,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MULTIPLE_LANGUAGES"
                          },
                          {
                            "enum_id": 75,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ICELANDIC_TRANSLATED"
                          },
                          {
                            "enum_id": 50,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 43,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IRISH_TRANSLATED"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ITALIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 57,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_JAPANESE_TRANSLATED"
                          },
                          {
                            "enum_id": 41,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_TRANSLATED"
                          },
                          {
                            "enum_id": 55,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KOREAN_TRANSLATED"
                          },
                          {
                            "enum_id": 40,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LATVIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 39,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LITHUANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 52,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MACEDONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 54,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAORI_TRANSLATED"
                          },
                          {
                            "enum_id": 19,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORWEGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 44,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_LANGUAGE"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_POLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 20,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PORTUGUESE_TRANSLATED"
                          },
                          {
                            "enum_id": 25,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ROMANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_RUSSIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 72,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SAMI_TRANSLATED"
                          },
                          {
                            "enum_id": 17,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAELIC_TRANSLATED"
                          },
                          {
                            "enum_id": 34,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SIMPLIFIED_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 22,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVAK_TRANSLATED"
                          },
                          {
                            "enum_id": 23,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 21,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SERBIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWEDISH_TRANSLATED"
                          },
                          {
                            "enum_id": 53,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TAMIL_TRANSLATED"
                          },
                          {
                            "enum_id": 45,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THAI_TRANSLATED"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TURKISH_TRANSLATED"
                          },
                          {
                            "enum_id": 27,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UKRAINIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 51,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIETNAMESE_TRANSLATED"
                          },
                          {
                            "enum_id": 24,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WELSH_TRANSLATED"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230840,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECONDARY_SUBTITLES",
                      "context": "secondary_subtitles",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 74,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALBANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 28,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARABIC_TRANSLATED"
                          },
                          {
                            "enum_id": 82,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARMENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 83,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AZERBAIJANI_TRANSLATED"
                          },
                          {
                            "enum_id": 48,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BAHASA_MELAYU_TRANSLATED"
                          },
                          {
                            "enum_id": 11,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BASQUE_TRANSLATED"
                          },
                          {
                            "enum_id": 37,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BULGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 12,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CATALAN_TRANSLATED"
                          },
                          {
                            "enum_id": 49,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 61,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MANDARIN_TRANSLATED"
                          },
                          {
                            "enum_id": 76,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CANTONESE_TRANSLATED"
                          },
                          {
                            "enum_id": 13,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CROATIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CZECH_TRANSLATED"
                          },
                          {
                            "enum_id": 14,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 15,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DUTCH_TRANSLATED"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ENGLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 26,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ESTONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 16,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FINNISH_TRANSLATED"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FRENCH_TRANSLATED"
                          },
                          {
                            "enum_id": 18,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GALLEGAN_TRANSLATED"
                          },
                          {
                            "enum_id": 84,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GEORGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GERMAN_TRANSLATED"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GREEK_TRANSLATED"
                          },
                          {
                            "enum_id": 29,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEBREW_TRANSLATED"
                          },
                          {
                            "enum_id": 58,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HINDI_TRANSLATED"
                          },
                          {
                            "enum_id": 30,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HUNGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 46,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_AUDIO"
                          },
                          {
                            "enum_id": 59,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECOND_AUDIO"
                          },
                          {
                            "enum_id": 60,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THIRD_AUDIO"
                          },
                          {
                            "enum_id": 47,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MULTIPLE_LANGUAGES"
                          },
                          {
                            "enum_id": 75,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ICELANDIC_TRANSLATED"
                          },
                          {
                            "enum_id": 50,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 43,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IRISH_TRANSLATED"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ITALIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 57,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_JAPANESE_TRANSLATED"
                          },
                          {
                            "enum_id": 41,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_TRANSLATED"
                          },
                          {
                            "enum_id": 55,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KOREAN_TRANSLATED"
                          },
                          {
                            "enum_id": 40,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LATVIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 39,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LITHUANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 52,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MACEDONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 54,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAORI_TRANSLATED"
                          },
                          {
                            "enum_id": 19,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORWEGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 44,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_LANGUAGE"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_POLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 20,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PORTUGUESE_TRANSLATED"
                          },
                          {
                            "enum_id": 25,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ROMANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_RUSSIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 72,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SAMI_TRANSLATED"
                          },
                          {
                            "enum_id": 17,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAELIC_TRANSLATED"
                          },
                          {
                            "enum_id": 34,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SIMPLIFIED_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 22,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVAK_TRANSLATED"
                          },
                          {
                            "enum_id": 23,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 21,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SERBIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWEDISH_TRANSLATED"
                          },
                          {
                            "enum_id": 53,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TAMIL_TRANSLATED"
                          },
                          {
                            "enum_id": 45,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THAI_TRANSLATED"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TURKISH_TRANSLATED"
                          },
                          {
                            "enum_id": 27,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UKRAINIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 51,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIETNAMESE_TRANSLATED"
                          },
                          {
                            "enum_id": 24,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WELSH_TRANSLATED"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230841,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PRIMARY_TELETEXT",
                      "context": "primary_text",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 74,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALBANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 28,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARABIC_TRANSLATED"
                          },
                          {
                            "enum_id": 82,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARMENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 83,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AZERBAIJANI_TRANSLATED"
                          },
                          {
                            "enum_id": 48,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BAHASA_MELAYU_TRANSLATED"
                          },
                          {
                            "enum_id": 11,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BASQUE_TRANSLATED"
                          },
                          {
                            "enum_id": 37,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BULGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 12,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CATALAN_TRANSLATED"
                          },
                          {
                            "enum_id": 49,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 61,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MANDARIN_TRANSLATED"
                          },
                          {
                            "enum_id": 76,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CANTONESE_TRANSLATED"
                          },
                          {
                            "enum_id": 13,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CROATIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CZECH_TRANSLATED"
                          },
                          {
                            "enum_id": 14,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 15,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DUTCH_TRANSLATED"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ENGLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 26,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ESTONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 16,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FINNISH_TRANSLATED"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FRENCH_TRANSLATED"
                          },
                          {
                            "enum_id": 18,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GALLEGAN_TRANSLATED"
                          },
                          {
                            "enum_id": 84,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GEORGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GERMAN_TRANSLATED"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GREEK_TRANSLATED"
                          },
                          {
                            "enum_id": 29,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEBREW_TRANSLATED"
                          },
                          {
                            "enum_id": 58,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HINDI_TRANSLATED"
                          },
                          {
                            "enum_id": 30,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HUNGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 46,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_AUDIO"
                          },
                          {
                            "enum_id": 59,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECOND_AUDIO"
                          },
                          {
                            "enum_id": 60,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THIRD_AUDIO"
                          },
                          {
                            "enum_id": 47,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MULTIPLE_LANGUAGES"
                          },
                          {
                            "enum_id": 75,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ICELANDIC_TRANSLATED"
                          },
                          {
                            "enum_id": 50,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 43,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IRISH_TRANSLATED"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ITALIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 57,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_JAPANESE_TRANSLATED"
                          },
                          {
                            "enum_id": 41,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_TRANSLATED"
                          },
                          {
                            "enum_id": 55,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KOREAN_TRANSLATED"
                          },
                          {
                            "enum_id": 40,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LATVIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 39,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LITHUANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 52,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MACEDONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 54,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAORI_TRANSLATED"
                          },
                          {
                            "enum_id": 19,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORWEGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 44,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_LANGUAGE"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_POLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 20,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PORTUGUESE_TRANSLATED"
                          },
                          {
                            "enum_id": 25,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ROMANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_RUSSIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 72,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SAMI_TRANSLATED"
                          },
                          {
                            "enum_id": 17,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAELIC_TRANSLATED"
                          },
                          {
                            "enum_id": 34,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SIMPLIFIED_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 22,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVAK_TRANSLATED"
                          },
                          {
                            "enum_id": 23,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 21,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SERBIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWEDISH_TRANSLATED"
                          },
                          {
                            "enum_id": 53,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TAMIL_TRANSLATED"
                          },
                          {
                            "enum_id": 45,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THAI_TRANSLATED"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TURKISH_TRANSLATED"
                          },
                          {
                            "enum_id": 27,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UKRAINIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 51,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIETNAMESE_TRANSLATED"
                          },
                          {
                            "enum_id": 24,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WELSH_TRANSLATED"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230842,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECONDARY_TELETEXT",
                      "context": "secondary_text",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 74,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ALBANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 28,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARABIC_TRANSLATED"
                          },
                          {
                            "enum_id": 82,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ARMENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 83,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AZERBAIJANI_TRANSLATED"
                          },
                          {
                            "enum_id": 48,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BAHASA_MELAYU_TRANSLATED"
                          },
                          {
                            "enum_id": 11,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BASQUE_TRANSLATED"
                          },
                          {
                            "enum_id": 37,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_BULGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 12,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CATALAN_TRANSLATED"
                          },
                          {
                            "enum_id": 49,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 61,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MANDARIN_TRANSLATED"
                          },
                          {
                            "enum_id": 76,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CANTONESE_TRANSLATED"
                          },
                          {
                            "enum_id": 13,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CROATIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CZECH_TRANSLATED"
                          },
                          {
                            "enum_id": 14,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 15,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_DUTCH_TRANSLATED"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ENGLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 26,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ESTONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 16,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FINNISH_TRANSLATED"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_FRENCH_TRANSLATED"
                          },
                          {
                            "enum_id": 18,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GALLEGAN_TRANSLATED"
                          },
                          {
                            "enum_id": 84,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GEORGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GERMAN_TRANSLATED"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GREEK_TRANSLATED"
                          },
                          {
                            "enum_id": 29,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEBREW_TRANSLATED"
                          },
                          {
                            "enum_id": 58,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HINDI_TRANSLATED"
                          },
                          {
                            "enum_id": 30,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HUNGARIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 46,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_AUDIO"
                          },
                          {
                            "enum_id": 59,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SECOND_AUDIO"
                          },
                          {
                            "enum_id": 60,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THIRD_AUDIO"
                          },
                          {
                            "enum_id": 47,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MULTIPLE_LANGUAGES"
                          },
                          {
                            "enum_id": 75,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ICELANDIC_TRANSLATED"
                          },
                          {
                            "enum_id": 50,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 43,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IRISH_TRANSLATED"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ITALIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 57,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_JAPANESE_TRANSLATED"
                          },
                          {
                            "enum_id": 41,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_TRANSLATED"
                          },
                          {
                            "enum_id": 55,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KOREAN_TRANSLATED"
                          },
                          {
                            "enum_id": 40,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LATVIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 39,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LITHUANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 52,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MACEDONIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 54,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MAORI_TRANSLATED"
                          },
                          {
                            "enum_id": 19,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORWEGIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 44,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ORIGINAL_LANGUAGE"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_POLISH_TRANSLATED"
                          },
                          {
                            "enum_id": 20,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PORTUGUESE_TRANSLATED"
                          },
                          {
                            "enum_id": 25,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ROMANIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_RUSSIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 72,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SAMI_TRANSLATED"
                          },
                          {
                            "enum_id": 17,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_GAELIC_TRANSLATED"
                          },
                          {
                            "enum_id": 34,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SIMPLIFIED_CHINESE_TRANSLATED"
                          },
                          {
                            "enum_id": 22,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVAK_TRANSLATED"
                          },
                          {
                            "enum_id": 23,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLOVENIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 21,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SERBIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPANISH_TRANSLATED"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWEDISH_TRANSLATED"
                          },
                          {
                            "enum_id": 53,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TAMIL_TRANSLATED"
                          },
                          {
                            "enum_id": 45,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_THAI_TRANSLATED"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TURKISH_TRANSLATED"
                          },
                          {
                            "enum_id": 27,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_UKRAINIAN_TRANSLATED"
                          },
                          {
                            "enum_id": 51,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIETNAMESE_TRANSLATED"
                          },
                          {
                            "enum_id": 24,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WELSH_TRANSLATED"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230843,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_POSTAL_CODE",
                "context": "postal_code",
                "data": {}
              },
              {
                "node_id": 2131230844,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_CLOCK",
                "context": "clock",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230845,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUTO_CLOCK_MODE",
                      "context": "auto_clock_mode",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUTOMATIC"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_COUNTRY_DEPENDENT"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MANUAL"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230846,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME_ZONE",
                      "context": "time_zone",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_WESTERN"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAZAKH_EASTERN"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230847,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME_ZONE",
                      "context": "time_zone",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PORTUGAL_MADEIRA"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_AZORES"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230848,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME_ZONE",
                      "context": "time_zone",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KALINGRAD"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_MOSCOW"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SAMARA"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_YEKATERINBURG"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OMSK"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KRASNOYARSK"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IRKUTSK"
                          },
                          {
                            "enum_id": 7,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_YAKUTSK"
                          },
                          {
                            "enum_id": 8,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VLADIVOSTOK"
                          },
                          {
                            "enum_id": 9,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SREDNEKOLYMSK"
                          },
                          {
                            "enum_id": 10,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_KAMCHATKA"
                          },
                          {
                            "enum_id": 11,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NONE"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230849,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME_ZONE",
                      "context": "time_zone",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPAIN_BALEARES"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CANARY_ISLANDS"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230850,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME_ZONE",
                      "context": "time_zone",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_QUEENSLAND"
                          },
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NEW_SOUTH_WALES"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_VICTORIA"
                          },
                          {
                            "enum_id": 5,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_TASMANIA"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SOUTH_AUSTRALIA"
                          },
                          {
                            "enum_id": 6,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NORTHERN_TERRITORY"
                          },
                          {
                            "enum_id": 4,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_WESTERN_AUSTRALIA"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230851,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME_ZONE",
                      "context": "time_zone",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIA_WESTERN_TIME_ZONE"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIA_CENTRAL_TIME_ZONE"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_INDONESIA_EASTERN_TIME_ZONE"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230852,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME_ZONE",
                      "context": "time_zone",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_NZ_EXCEPT_CHATHAM_TIME_ZONE"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHATHAM_ISLANDS"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230853,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_DATE",
                      "context": "date",
                      "data": {},
                      "type": "DATE_PICKER"
                    },
                    {
                      "node_id": 2131230854,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TIME",
                      "context": "time",
                      "data": {},
                      "type": "TIME_PICKER"
                    },
                    {
                      "node_id": 2131230855,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SLEEPTIMER",
                      "context": "sleeptimer",
                      "data": {
                        "slider_data": {
                          "min": 0,
                          "max": 180,
                          "step_size": 5
                        }
                      },
                      "type": "SLIDER_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230856,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_RC_KEYBOARD",
                "context": "rc_keyboard",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_QWERTY"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MISC_AZERTY"
                    }
                  ]
                },
                "type": "LIST_NODE"
              }
            ]
          }
        },
        {
          "node_id": 2131230754,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_GOOGLE_SETTINGS",
          "context": "android_settings",
          "data": {}
        },
        {
          "node_id": 2131230755,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_UNIVERSAL_ACCESS",
          "context": "accessibility",
          "data": {
            "nodes": [
              {
                "node_id": 2131230756,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_UNIVERSAL_ACCESS",
                "context": "universal_access",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230757,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEARING_IMPAIRED",
                "context": "hearing_impaired",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230758,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUDIO_DESCRIPTION",
                "context": "audio_description_menu",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230759,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUDIO_DESCRIPTION",
                      "context": "audio_description",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230760,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPEAKERS_OR_HEADPHONES",
                      "context": "speakers_headphones",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPEAKERS"
                          },
                          {
                            "enum_id": 2,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_HEADPHONE"
                          },
                          {
                            "enum_id": 3,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPEAKERS_HEADPHONE"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230761,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_MIXED_VOLUME",
                      "context": "mixed_volume",
                      "data": {
                        "slider_data": {
                          "min": -32,
                          "max": 32,
                          "step_size": 1
                        }
                      },
                      "type": "SLIDER_NODE"
                    },
                    {
                      "node_id": 2131230762,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SEAMLESS_MIXING",
                      "context": "audio_effects",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230763,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SPEECH_PREFERENCE",
                      "context": "speech",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PREFERENCE_DESCRIPTIVE"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PREFERENCE_SUBTITLES"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    }
                  ]
                }
              },
              {
                "node_id": 2131230764,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_DIALOGUE_ENHANCEMENT",
                "context": "dialogue_enhancement",
                "data": {
                  "slider_data": {
                    "min": 0,
                    "max": 9,
                    "step_size": 1
                  }
                },
                "type": "SLIDER_NODE"
              }
            ]
          }
        },
        {
          "node_id": 2131230823,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHILD_LOCK",
          "context": "child_lock",
          "data": {
            "nodes": [
              {
                "node_id": 2131230824,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_PARENTAL_RATING",
                "context": "parental_rating",
                "data": {
                  "enums": []
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230825,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_PARENTAL_RATING_STREAMING_CHANNELS",
                "context": "parental_rating",
                "data": {
                  "nodes": [
                    {
                      "node_id": 900001,
                      "type": "PARENT_NODE",
                      "string_id": "Argentina",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900038,
                            "string_id": "ATP",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900039,
                            "string_id": "SAM 13",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900040,
                            "string_id": "SAM 16",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900041,
                            "string_id": "SAM 18",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900002,
                      "type": "PARENT_NODE",
                      "string_id": "Australien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900042,
                            "type": "PARENT_NODE",
                            "string_id": "P",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900043,
                            "type": "PARENT_NODE",
                            "string_id": "C",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900044,
                            "type": "PARENT_NODE",
                            "string_id": "G",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900045,
                            "type": "PARENT_NODE",
                            "string_id": "PG",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900046,
                            "type": "PARENT_NODE",
                            "string_id": "M",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900047,
                            "type": "PARENT_NODE",
                            "string_id": "MA",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900048,
                            "type": "PARENT_NODE",
                            "string_id": "AV",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900049,
                            "type": "PARENT_NODE",
                            "string_id": "R",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900003,
                      "type": "PARENT_NODE",
                      "string_id": "Brasilien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900050,
                            "string_id": "GA",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900051,
                            "string_id": "PG-10",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900052,
                            "string_id": "PG-12",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900053,
                            "string_id": "PG-14",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900054,
                            "string_id": "PG-16",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          },
                          {
                            "node_id": 900055,
                            "string_id": "PG-18",
                            "context": "parental_rating",
                            "data": {
                              "enums": []
                            },
                            "type": "LIST_NODE"
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900004,
                      "type": "PARENT_NODE",
                      "string_id": "Kanada",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900056,
                            "type": "PARENT_NODE",
                            "string_id": "E",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900057,
                            "type": "PARENT_NODE",
                            "string_id": "C",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900058,
                            "type": "PARENT_NODE",
                            "string_id": "C8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900059,
                            "type": "PARENT_NODE",
                            "string_id": "G",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900060,
                            "type": "PARENT_NODE",
                            "string_id": "PG",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900061,
                            "type": "PARENT_NODE",
                            "string_id": "14+",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900062,
                            "type": "PARENT_NODE",
                            "string_id": "18+",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900005,
                      "type": "PARENT_NODE",
                      "string_id": "Kina",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900063,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900064,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900065,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900066,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900067,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900068,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900069,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900070,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900071,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900072,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900073,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900074,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900075,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900076,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900077,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900006,
                      "type": "PARENT_NODE",
                      "string_id": "Armenien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900078,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900079,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900080,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900081,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900082,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900083,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900084,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900085,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900086,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900087,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900088,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900089,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900090,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900091,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900092,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900007,
                      "type": "PARENT_NODE",
                      "string_id": "Bulgarien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900093,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900094,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900095,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900096,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900097,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900098,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900099,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900100,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900101,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900102,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900103,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900104,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900105,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900106,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900107,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900008,
                      "type": "PARENT_NODE",
                      "string_id": "Schweiz",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900108,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900109,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900110,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900111,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900112,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900113,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900114,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900115,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900116,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900117,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900118,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900119,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900120,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900121,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900122,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900009,
                      "type": "PARENT_NODE",
                      "string_id": "Tyskland",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900123,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900124,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900125,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900126,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900127,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900128,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900129,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900130,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900131,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900132,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900133,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900134,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900135,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900136,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900137,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900010,
                      "type": "PARENT_NODE",
                      "string_id": "Danmark",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900138,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900139,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900140,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900141,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900142,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900143,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900144,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900145,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900146,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900147,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900148,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900149,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900150,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900151,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900152,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900011,
                      "type": "PARENT_NODE",
                      "string_id": "Finland",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900153,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900154,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900155,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900156,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900157,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900158,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900159,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900160,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900161,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900162,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900163,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900164,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900165,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900166,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900167,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900012,
                      "type": "PARENT_NODE",
                      "string_id": "Grekland",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900168,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900169,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900170,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900171,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900172,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900173,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900174,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900175,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900176,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900177,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900178,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900179,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900180,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900181,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900182,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900013,
                      "type": "PARENT_NODE",
                      "string_id": "Ungern",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900183,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900184,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900185,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900186,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900187,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900188,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900189,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900190,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900191,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900192,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900193,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900194,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900195,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900196,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900197,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900014,
                      "type": "PARENT_NODE",
                      "string_id": "Indonesien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900198,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900199,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900200,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900201,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900202,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900203,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900204,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900205,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900206,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900207,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900208,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900209,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900210,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900211,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900212,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900015,
                      "type": "PARENT_NODE",
                      "string_id": "Irland",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900213,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900214,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900215,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900216,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900217,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900218,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900219,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900220,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900221,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900222,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900223,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900224,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900225,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900226,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900227,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900016,
                      "type": "PARENT_NODE",
                      "string_id": "Israel",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900228,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900229,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900230,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900231,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900232,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900233,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900234,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900235,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900236,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900237,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900238,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900239,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900240,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900241,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900242,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900017,
                      "type": "PARENT_NODE",
                      "string_id": "Island",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900243,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900244,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900245,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900246,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900247,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900248,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900249,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900250,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900251,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900252,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900253,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900254,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900255,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900256,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900257,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900018,
                      "type": "PARENT_NODE",
                      "string_id": "Malaysia",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900258,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900259,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900260,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900261,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900262,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900263,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900264,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900265,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900266,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900267,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900268,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900269,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900270,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900271,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900272,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900019,
                      "type": "PARENT_NODE",
                      "string_id": "Nederl\u00e4nderna",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900273,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900274,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900275,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900276,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900277,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900278,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900279,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900280,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900281,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900282,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900283,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900284,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900285,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900286,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900287,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900020,
                      "type": "PARENT_NODE",
                      "string_id": "Nya Zeeland",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900288,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900289,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900290,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900291,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900292,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900293,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900294,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900295,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900296,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900297,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900298,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900299,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900300,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900301,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900302,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900021,
                      "type": "PARENT_NODE",
                      "string_id": "Polen",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900303,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900304,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900305,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900306,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900307,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900308,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900309,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900310,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900311,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900312,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900313,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900314,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900315,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900316,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900317,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900022,
                      "type": "PARENT_NODE",
                      "string_id": "Portugal",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900318,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900319,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900320,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900321,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900322,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900323,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900324,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900325,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900326,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900327,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900328,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900329,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900330,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900331,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900332,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900023,
                      "type": "PARENT_NODE",
                      "string_id": "Rum\u00e4nien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900333,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900334,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900335,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900336,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900337,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900338,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900339,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900340,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900341,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900342,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900343,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900344,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900345,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900346,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900347,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900024,
                      "type": "PARENT_NODE",
                      "string_id": "Ryssland",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900348,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900349,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900350,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900351,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900352,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900353,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900354,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900355,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900356,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900357,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900358,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900359,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900360,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900361,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900362,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900025,
                      "type": "PARENT_NODE",
                      "string_id": "Serbien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900363,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900364,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900365,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900366,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900367,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900368,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900369,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900370,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900371,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900372,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900373,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900374,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900375,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900376,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900377,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900026,
                      "type": "PARENT_NODE",
                      "string_id": "Slovenien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900378,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900379,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900380,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900381,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900382,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900383,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900384,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900385,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900386,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900387,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900388,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900389,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900390,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900391,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900392,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900027,
                      "type": "PARENT_NODE",
                      "string_id": "Thailand",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900393,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900394,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900395,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900396,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900397,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900398,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900399,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900400,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900401,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900402,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900403,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900404,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900405,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900406,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900407,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900028,
                      "type": "PARENT_NODE",
                      "string_id": "Turkiet",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900408,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900409,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900410,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900411,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900412,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900413,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900414,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900415,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900416,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900417,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900418,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900419,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900420,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900421,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900422,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900029,
                      "type": "PARENT_NODE",
                      "string_id": "Taiwan",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900423,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900424,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900425,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900426,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900427,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900428,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900429,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900430,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900431,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900432,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900433,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900434,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900435,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900436,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900437,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900030,
                      "type": "PARENT_NODE",
                      "string_id": "Ukraina",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900438,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900439,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900440,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900441,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900442,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900443,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900444,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900445,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900446,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900447,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900448,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900449,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900450,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900451,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900452,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900031,
                      "type": "PARENT_NODE",
                      "string_id": "Spanien",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900453,
                            "type": "PARENT_NODE",
                            "string_id": "All",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900454,
                            "type": "PARENT_NODE",
                            "string_id": "Children",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900455,
                            "type": "PARENT_NODE",
                            "string_id": "X-Rated",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900456,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900457,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900458,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900459,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900460,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900461,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900462,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900463,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900464,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900465,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900466,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900467,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900468,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900469,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900470,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900032,
                      "type": "PARENT_NODE",
                      "string_id": "Frankrike",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900471,
                            "type": "PARENT_NODE",
                            "string_id": "Universal",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900472,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900473,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900474,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900475,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900476,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900477,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900478,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900479,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900480,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900481,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900482,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900483,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900484,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900485,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900486,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900033,
                      "type": "PARENT_NODE",
                      "string_id": "Japan",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900487,
                            "type": "PARENT_NODE",
                            "string_id": "4",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900488,
                            "type": "PARENT_NODE",
                            "string_id": "5",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900489,
                            "type": "PARENT_NODE",
                            "string_id": "6",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900490,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900491,
                            "type": "PARENT_NODE",
                            "string_id": "8",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900492,
                            "type": "PARENT_NODE",
                            "string_id": "9",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900493,
                            "type": "PARENT_NODE",
                            "string_id": "10",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900494,
                            "type": "PARENT_NODE",
                            "string_id": "11",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900495,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900496,
                            "type": "PARENT_NODE",
                            "string_id": "13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900497,
                            "type": "PARENT_NODE",
                            "string_id": "14",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900498,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900499,
                            "type": "PARENT_NODE",
                            "string_id": "16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900500,
                            "type": "PARENT_NODE",
                            "string_id": "17",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900501,
                            "type": "PARENT_NODE",
                            "string_id": "18",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900502,
                            "type": "PARENT_NODE",
                            "string_id": "19",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900503,
                            "type": "PARENT_NODE",
                            "string_id": "20",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900034,
                      "type": "PARENT_NODE",
                      "string_id": "Sydkorea",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900504,
                            "type": "PARENT_NODE",
                            "string_id": "ALL",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900505,
                            "type": "PARENT_NODE",
                            "string_id": "7",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900506,
                            "type": "PARENT_NODE",
                            "string_id": "12",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900507,
                            "type": "PARENT_NODE",
                            "string_id": "15",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900508,
                            "type": "PARENT_NODE",
                            "string_id": "19",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900035,
                      "type": "PARENT_NODE",
                      "string_id": "Singapore",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900509,
                            "type": "PARENT_NODE",
                            "string_id": "G",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900510,
                            "type": "PARENT_NODE",
                            "string_id": "PG",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900511,
                            "type": "PARENT_NODE",
                            "string_id": "PG13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900512,
                            "type": "PARENT_NODE",
                            "string_id": "NC16",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900513,
                            "type": "PARENT_NODE",
                            "string_id": "M18",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900514,
                            "type": "PARENT_NODE",
                            "string_id": "R21",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 900036,
                      "type": "PARENT_NODE",
                      "string_id": "USA",
                      "context": "parental_rating",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 900515,
                            "type": "PARENT_NODE",
                            "string_id": "G",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900516,
                            "type": "PARENT_NODE",
                            "string_id": "PG",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900517,
                            "type": "PARENT_NODE",
                            "string_id": "PG-13",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900518,
                            "type": "PARENT_NODE",
                            "string_id": "R",
                            "context": "parental_rating",
                            "data": {}
                          },
                          {
                            "node_id": 900519,
                            "type": "PARENT_NODE",
                            "string_id": "NC-17",
                            "context": "parental_rating",
                            "data": {}
                          }
                        ]
                      }
                    }
                  ]
                }
              },
              {
                "node_id": 2131230826,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_APP_LOCKING",
                "context": "app_locking",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230827,
                "type": "PARENT_NODE",
                "context": "change_code",
                "data": {}
              },
              {
                "node_id": 2131230828,
                "type": "PARENT_NODE",
                "context": "CAM_change_code",
                "data": {}
              }
            ]
          }
        },
        {
          "node_id": 2131230724,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_WIRELESS_AND_NETWORKS",
          "context": "wireless_networks",
          "data": {
            "nodes": [
              {
                "node_id": 2131230725,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_WIRED_OR_WIFI",
                "context": "network",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230726,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CONNECT_TO_NETWORK",
                      "context": "connect_to_network",
                      "data": {}
                    },
                    {
                      "node_id": 2131230727,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIEW_NETWORK_SETTINGS",
                      "context": "view_network_settings",
                      "data": {}
                    },
                    {
                      "node_id": 2131230728,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_NETWORK_MODE",
                      "context": "network_configuration",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MISC_DHCP"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_STATIC_IP"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230729,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_IP_CONFIGURATION",
                      "context": "ip_configuration",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230730,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PANEL_IPV4_ADDRESS",
                            "context": "ip_address",
                            "data": {}
                          },
                          {
                            "node_id": 2131230731,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PANEL_IPV4_NETMASK",
                            "context": "netmask",
                            "data": {}
                          },
                          {
                            "node_id": 2131230732,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PANEL_IPV4_GATEWAY",
                            "context": "gateway",
                            "data": {}
                          },
                          {
                            "node_id": 2131230733,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PANEL_IPV4_DNS_1",
                            "context": "dns_1",
                            "data": {}
                          },
                          {
                            "node_id": 2131230734,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_PANEL_IPV4_DNS_2",
                            "context": "dns_2",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230735,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWITCH_ON_WITH_WIFI_WOWLAN",
                      "context": "switch_on_with_network",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230736,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SWITCH_ON_WITH_CHROMECAST",
                      "context": "switch_on_with_network",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230737,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_RENDERER_ACCESS",
                      "context": "digital_media_renderer",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230738,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_WIFI_ON_OFF",
                      "context": "wifi_on_off",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230739,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_RECORDING_ON_THE_GO",
                      "context": "myremote_recording",
                      "data": {}
                    },
                    {
                      "node_id": 2131230740,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_TV_NAME",
                      "context": "tv_network_name",
                      "data": {},
                      "type": "TEXT_ENTRY"
                    },
                    {
                      "node_id": 2131230741,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CLEAR_APPS_MEMORY",
                      "context": "clear_internet_memory",
                      "data": {}
                    }
                  ]
                }
              },
              {
                "node_id": 2131230742,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_BLUETOOTH",
                "context": "bluetooth",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230743,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_BT_ON_OFF",
                      "context": "bluetooth_on_off",
                      "data": {
                        "enums": [
                          {
                            "enum_id": 0,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                          },
                          {
                            "enum_id": 1,
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                          }
                        ]
                      },
                      "type": "LIST_NODE"
                    },
                    {
                      "node_id": 2131230744,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_SEARCH_BT_DEVICE",
                      "context": "search_for_bt_devices",
                      "data": {}
                    },
                    {
                      "node_id": 2131230745,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_REMOVE_BT_DEVICE",
                      "context": "remove_bt_device",
                      "data": {}
                    }
                  ]
                }
              },
              {
                "node_id": 2131230746,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_REMOTE_CONTROL",
                "context": "bt_remote_control",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230747,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PAIR_RC",
                      "context": "pair_remote_control",
                      "data": {}
                    },
                    {
                      "node_id": 2131230748,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_REMOTE_CONTROL_INFO",
                      "context": "check_software_version",
                      "data": {}
                    },
                    {
                      "node_id": 2131230749,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CH_UPDATE_RC_SOFTWARE",
                      "context": "update_rc_software",
                      "data": {}
                    }
                  ]
                }
              },
              {
                "node_id": 2131230750,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_CUBE_NAME",
                "context": "cube_name",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230751,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_PAIR_CUBE_NAME",
                      "context": "pair_voice_cube",
                      "data": {}
                    },
                    {
                      "node_id": 2131230748,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CURRENT_SOFTWARE_INFO",
                      "context": "check_software_version",
                      "data": {}
                    },
                    {
                      "node_id": 2131230752,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_UPDATE_CUBE_NAME_SOFTWARE",
                      "context": "update_rc_software",
                      "data": {}
                    }
                  ]
                }
              }
            ]
          }
        },
        {
          "node_id": 2131230816,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_CHANNELS",
          "context": "channels",
          "data": {
            "nodes": [
              {
                "node_id": 2131230817,
                "type": "PARENT_NODE",
                "context": "channel_installation",
                "data": {}
              },
              {
                "node_id": 2131230818,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_SATELLITE_INSTALLATION",
                "context": "satellite_installation",
                "data": {}
              },
              {
                "node_id": 2131230819,
                "type": "PARENT_NODE",
                "context": "channel_list_copy",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230820,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_COPY_TO_USB",
                      "context": "channels_copy_to_usb",
                      "data": {}
                    },
                    {
                      "node_id": 2131230821,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_COPY_TO_TV",
                      "context": "channels_copy_to_tv",
                      "data": {}
                    },
                    {
                      "node_id": 2131230822,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_CURRENT_VERSION",
                      "context": "channels_current_version",
                      "data": {}
                    }
                  ]
                }
              }
            ]
          }
        },
        {
          "node_id": 2131230977,
          "type": "PARENT_NODE",
          "string_id": "org.droidtv.ui.strings.R.string.MAIN_UPDATE_SOFTWARE",
          "context": "update_software",
          "data": {
            "nodes": [
              {
                "node_id": 2131230978,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_SEARCH_FOR_UPDATES",
                "context": "search_for_update",
                "data": {
                  "nodes": [
                    {
                      "node_id": 2131230979,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_INTERNET_RECOMMENDED",
                      "context": "internet_updates",
                      "data": {}
                    },
                    {
                      "node_id": 2131230980,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_USB",
                      "context": "local_updates",
                      "data": {
                        "nodes": [
                          {
                            "node_id": 2131230981,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOCAL_UPDATES",
                            "context": "local_updates",
                            "data": {}
                          },
                          {
                            "node_id": 2131230982,
                            "type": "PARENT_NODE",
                            "string_id": "org.droidtv.ui.strings.R.string.MAIN_IDENTIFY_TV",
                            "context": "local_updates",
                            "data": {}
                          }
                        ]
                      }
                    },
                    {
                      "node_id": 2131230983,
                      "type": "PARENT_NODE",
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_LOOK_FOR_OAD_UPDATES",
                      "context": "look_for_oad_updates",
                      "data": {}
                    }
                  ]
                }
              },
              {
                "node_id": 2131230984,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_CURRENT_SOFTWARE_INFO",
                "context": "current_software_info",
                "data": {}
              },
              {
                "node_id": 2131230985,
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_AUTOMATIC_SOFTWARE_UPDATE",
                "context": "automatic_update",
                "data": {
                  "enums": [
                    {
                      "enum_id": 0,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_OFF"
                    },
                    {
                      "enum_id": 1,
                      "string_id": "org.droidtv.ui.strings.R.string.MAIN_ON"
                    }
                  ]
                },
                "type": "LIST_NODE"
              },
              {
                "node_id": 2131230986,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_ANNOUNCEMENT",
                "context": "announcement",
                "data": {}
              },
              {
                "node_id": 2131230987,
                "type": "PARENT_NODE",
                "string_id": "org.droidtv.ui.strings.R.string.MAIN_VIEW_SOFTWARE_UPDATE_HISTORY",
                "context": "view_software_update_history",
                "data": {}
              }
            ]
          }
        }
      ]
    }
  }
}

MENUITEMS_SETTINGS_UPDATE: MenuItemsSettingsUpdate = {
    "values": [
        {
            "value": {
                "Nodeid": 2131230778,
                "data": {
                    "value": True
                }
            }
        }
    ]
}

MENUITEMS_SETTINGS_CURRENT: MenuItemsSettingsCurrent = {
    "values": [
        {
            "value": {
                "Nodeid": 2131230778,
                "Controllable": False,
                "Available": True,
                "string_id": "Inschakelen",
                "data": {
                    "value": True
                }
            }
        }
    ],
    "version": 0
}

MENUITEMS_SETTINGS_CURRENT_POST: MenuItemsSettingsCurrentPost = {
    "nodes": [
        {
            "nodeid": 420
        }
    ]
}