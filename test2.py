from haphilipsjs.typing import ApplicationIntentType
from haphilipsjs import AUTH_SHARED_KEY, PhilipsTV, cbc_decode
import logging
import pprint
from datetime import datetime
import asyncio

import haphilipsjs
pp = pprint.PrettyPrinter(depth=4)

logging.basicConfig(level=logging.DEBUG)

async def main():
    tv = PhilipsTV("tv2.ecce.loc", 6, 
    username='7669647ae9ae2e3bdec2ecdc083cae5e',
    password='168a45bcfb40dac840880ee60b75687fc9124ead41421efb5c366df18c49728d')

    #pp.pprint(tv._getReq("system/timestamp"))
    #await tv.update()
    await tv.setTransport(True)

    #pp.pprint(tv.powerstate)
    #pp.pprint(tv.system)

    #pp.pprint(tv.getChannelLists())
    #pp.pprint(tv.applications)
    #pp.pprint(tv.application)
    #pp.pprint(tv.screenstate)
    #tv.sendKey("PlayPause")
    #tv.sendUnicode(chr(32))

    #pp.pprint(tv._getReq("channeldb/tv/favoriteLists/all"))

    #pp.pprint(tv._getReq("channeldb/tv/channels/current"))

    #pp.pprint(tv._getReq("companionlauncher/launch_response"))
    #pp.pprint(tv.channels)
    #logo = tv.getChannelLogo(1)

    #logo, contenttype = tv.getApplicationIcon("com.ted.android.tv.view.MainActivity-com.ted.android.tv")
    #if logo:
    #    with open("logo.png", "wb") as f:
    #        f.write(logo)
    #else:
    #    print("Can't find logo")

    #print("256)

    #tv.sendUnicode("\u00f4")
    #tv.sendUnicode("KEYCODE_TV_INPUT_HDMI_1")
    #tv.sendUnicode("a")
    #for i in range(256, 512):
    #    tv.sendUnicode(chr(i))
    #tv.sendUnicode(chr(228))
    #tv.sendUnicode("\r")
    #tv.sendUnicode("\u2421")


    #pp.pprint(tv.channel)
    #pp.pprint(tv.getAmbilightProcessed())
    #while True:
    #    print(datetime.now())
    #    pp.pprint(tv.notifyChange(5*60))
 



    #adb shell am start
    #  -a android.intent.action.VIEW 
    #  -d content://android.media.tv/passthrough/org.droidtv.hdmiService%2F.HdmiService%2FHW9
    #  -n org.droidtv.zapster/.playtv.activity.PlayTvActivity
    #  -f 0x10000000


    # intent: ApplicationIntentType = {
    #     "extras": { "uri": "HDMI 4" },
    #     "action": "Intent {  act=android.intent.action.ASSIST cmp=com.google.android.katniss/com.google.android.apps.tvsearch.app.launch.trampoline.SearchActivityTrampoline flg=0x10200000 }", 
    #     "component": {
    #         "packageName": "com.google.android.katniss",
    #         "className": "com.google.android.apps.tvsearch.app.launch.trampoline.SearchActivityTrampoline"
    #     }
    # }


    # intent: ApplicationIntentType = {
    #     "extras": { "query": "HDMI 4" },
    #     "action": "android.intent.action.ASSIST",
    #     "component": {
    #         "packageName": "com.google.android.katniss",
    #         "className": "com.google.android.apps.tvsearch.app.launch.trampoline.SearchActivityTrampoline"
    #     }
    # }

# 02-06 03:19:54.531  2322  3083 I ActivityManager: START u0 {act=android.intent.action.VIEW dat=content://android.media.tv/passthrough/com.mediatek.tvinput/.hdmi.HDMIInputService/HW5 flg=0x10000000 cmp=org.droidtv.playtv/.PlayTvActivity (has extras)} from uid 1000

#Intent {
# act=android.intent.action.VIEW
# dat=content://android.media.tv/passthrough/com.mediatek.tvinput/.hdmi.HDMIInputService/HW5
# flg=0x10000000
# cmp=org.droidtv.playtv/.PlayTvActivity (has extras)}", 


# 10-14 10:18:16.654  5058  5058 D SourceElementCallback: onElementClick position:7
# 10-14 10:18:16.656  5058  5058 W ContextImpl: Calling a method in the system process without a qualified user: android.app.ContextImpl.bindService:1611 android.content.ContextWrapper.bindService:698 org.droidtv.channels.sources.SourcesUtils.bindToLoggingService:743 org.droidtv.channels.sources.SourcesUtils.switchTo:327 org.droidtv.channels.sources.SourceElementCallback.onElementClick:82
# 10-14 10:18:16.658  5058  5058 D SourcesUtils: PASSTHROUGH sourceUri:content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW5
# 10-14 10:18:16.660  3878  3972 D org.droidtv.candeebug.Gateway: Returning successfully for event: {"event-type":"unknown.28","boot-count":9,"standby-count":9,"kernel-time":4030979,"data":{"original-event-type":28,"InputName":"Computer","uiname":"HDMI 1","ver":1}}
# 10-14 10:18:16.661  3878  5242 D org.droidtv.candeebug.h.a: Updated total event size to: 6815
# 10-14 10:18:16.670  2325  5682 I ActivityManager: START u0 {act=android.intent.action.VIEW dat=content://android.media.tv/passthrough/com.mediatek.tvinput/.hdmi.HDMIInputService/HW5 flg=0x10000000 cmp=org.droidtv.playtv/.PlayTvActivity (has extras)} from uid 1000
# 10-14 10:18:16.673  3540  3540 D PlayTvActivity: onNewIntent Action android.intent.action.VIEW data content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW5
# 10-14 10:18:16.673  3540  3540 D PlayTvActivity: device ID =5
# 10-14 10:18:16.673  3540  3540 D PlayTvActivity: onNewIntent: ACTION_VIEW fav_list_id -1
# 10-14 10:18:16.685  3540  3540 D PlayTvActivity: onResume STATE_STARTED
# 10-14 10:18:16.686  3540  3540 D TvSessionManager: setStreamType value true

#        "action": "Intent {act=android.intent.action.VIEW dat=content://android.media.tv/passthrough/com.mediatek.tvinput/.hdmi.HDMIInputService/HW5 flg=0x10000000 cmp=org.droidtv.playtv/.PlayTvActivity (has extras)}", 

#     intent1: ApplicationIntentType = {
#         "extras": { "device-id": "5" },
#         "data": "content://android.media.tv/passthrough/com.mediatek.tvinput/.hdmi.HDMIInputService/HW5",
#         "action": "android.intent.action.VIEW", 
#         "component": {
#             "packageName": "org.droidtv.playtv",
#             "className": "org.droidtv.playtv.PlayTvActivity"
#         }
#     }


#     intent1: ApplicationIntentType = {
#         "extras": { "data": "content://android.media.tv/passthrough/com.mediatek.tvinput/.hdmi.HDMIInputService/HW5" },
# #        "data": "content://android.media.tv/passthrough/com.mediatek.tvinput/.hdmi.HDMIInputService/HW5",
#         "action": "android.intent.action.VIEW", 
#         "component": {
#             "packageName": "org.droidtv.playtv",
#             "className": "org.droidtv.playtv.PlayTvActivity"
#         }
#     }



#     intent2: ApplicationIntentType = {
#         #"extras": { "EXTRA_KEY_EVENT": { "action":"ACTION_DOWN", "keyCode":"KEYCODE_TV_INPUT_HDMI_1", "scanCode":0, "metaState":0, "flags":0x0, "repeatCount":0, "eventTime":78217285, "downTime":78217285, "deviceId":-1, "source":0x101 } },
#         "extras": { "EXTRA_KEY_EVENT": "KEYCODE_TV_INPUT_HDMI_1" },
#         "action": "android.intent.action.MEDIA_BUTTON", 
#         "component": {
#             "packageName": "org.droidtv.playtv",
#             "className": "org.droidtv.playtv.PlayTvActivity"
#         }
#     }


# 02-20 17:01:18.552  6033  6180 D SourcesElementInfo: SourcesElementInfo(HDMI 4, null, 0, android.graphics.drawable.StateListDrawable@b8dcb8a, com.mediatek.tvinput/.hdmi.HDMIInputService/HW8, null, 1007, 2, true, android.graphics.drawable.StateListDrawable@61fe5fb, false)
# 02-20 17:01:18.555  6033  6180 D SourcesElementInfo: SourcesElementInfo(HDMI 3, null, 0, android.graphics.drawable.StateListDrawable@ec99618, com.mediatek.tvinput/.hdmi.HDMIInputService/HW7, null, 1007, 2, true, android.graphics.drawable.StateListDrawable@6206871, false)
# 02-20 17:01:18.558  6033  6180 D SourcesElementInfo: SourcesElementInfo(HDMI 2, null, 0, android.graphics.drawable.StateListDrawable@4051656, com.mediatek.tvinput/.hdmi.HDMIInputService/HW6, null, 1007, 2, true, android.graphics.drawable.StateListDrawable@f7ce6d7, false)
# 02-20 17:01:18.565  6033  6180 D SourcesElementInfo: SourcesElementInfo(ARCAM AVR, HDMI 1, 0, android.graphics.drawable.StateListDrawable@7cdfbc4, com.mediatek.tvinput/.hdmi.HDMIInputService/HW5, null, 1007, 2, true, android.graphics.drawable.StateListDrawable@3021aad, false)
# 02-20 17:01:18.577  6033  6180 D SourcesElementInfo: SourcesElementInfo(ARCAM AVR, HDMI 1 / MHL, 0, android.graphics.drawable.StateListDrawable@5f82b3a, com.mediatek.tvinput/.hdmi.HDMIInputService/HW5, null, 5, 0, true, android.graphics.drawable.StateListDrawable@b243eb, false)
# 02-20 17:01:18.588  6033  6180 D SourcesElementInfo: SourcesElementInfo(Chromecast Bi, HDMI 4, 0, android.graphics.drawable.StateListDrawable@f5ab548, com.mediatek.tvinput/.hdmi.HDMIInputService/HW8, null, 4, 0, true, android.graphics.drawable.StateListDrawable@a8b4fe1, false)
# 02-20 17:01:18.589  6033  6180 D SourcesService: createSourceList  tvinputid  : com.mediatek.tvinput/.hdmi.HDMIInputService/HW8,  tvinput_num : 3
# 02-20 17:01:18.589  6033  6180 D SourcesService: SourcesElementsList  i : 7,  PrimaryText : ARCAM AVR,  getTvInputId : com.mediatek.tvinput/.hdmi.HDMIInputService/HW5
# 02-20 17:01:18.590  6033  6180 D SourcesService: SourcesElementsList  i : 8,  PrimaryText : Chromecast Bi,  getTvInputId : com.mediatek.tvinput/.hdmi.HDMIInputService/HW8
# 02-20 17:01:18.612  6033  6180 D SourcesService: oneTvInputId value to check com.mediatek.tvinput/.hdmi.HDMIInputService/HW8
# 02-20 17:01:18.612  6033  6180 D SourcesService: oneTvInputId value to check com.mediatek.tvinput/.hdmi.HDMIInputService/HW7
# 02-20 17:01:18.612  6033  6180 D SourcesService: oneTvInputId value to check com.mediatek.tvinput/.hdmi.HDMIInputService/HW6
# 02-20 17:01:18.612  6033  6180 D SourcesService: oneTvInputId value to check com.mediatek.tvinput/.hdmi.HDMIInputService/HDMI400008
# 02-20 17:01:18.612  6033  6180 D SourcesService: oneTvInputId value to check com.mediatek.tvinput/.hdmi.HDMIInputService/HW5

    intent: ApplicationIntentType = {
        #"extras": { "uri": "content://android.media.tv/passthrough/org.droidtv.hdmiService%2F.HdmiService%2FHW10" },
        "extras": { "uri": "content://android.media.tv/passthrough/com.mediatek.tvinput%2F.hdmi.HDMIInputService%2FHW8" },
        "action": "org.droidtv.playtv.SELECTURI",
        "component": {
            "packageName": "org.droidtv.playtv",
            "className": "org.droidtv.playtv.PlayTvActivity"
        }
    }

    await tv.setApplication(intent)

    #pp.pprint(tv.system)
    #print(haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, system["model_encrypted"]))

#    print(haphilipsjs.hmac_signature(b"abcd", "haha", "hooho"))
#    print(haphilipsjs.hmac_signature_old(b"abcd", "haha", "hooho"))


    #data_encrypted = haphilipsjs.cbc_encode(haphilipsjs.AUTH_SHARED_KEY, "1234567890")
    #data = haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, data_encrypted)
    #print(data_encrypted)
    #print(data)
    
    #print(haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, "i4Ea4UC2cBqOH8sPyvElT2APuqHfzMHCqTLnbMVse5k=\n"))
    #print(haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, "z3eXiQ4C3gPpqqjyUtXF3zcra0PyISaPOiUIdycA/OEChdh4wv/VcEFBv9J3K4Vc\n")
    #print(tv.getApplications())
    #pp.pprint(tv.getApplicationId())
    #pp.pprint(tv.channels)
    #print(tv.getChannels())
    #print(tv.getChannelId())
    #pp.pprint(tv._getReq("audio/volume"))
    #pp.pprint(tv._getReq("activities/tv"))
    await tv.aclose()


#('7669647ae9ae2e3bdec2ecdc083cae5e', '168a45bcfb40dac840880ee60b75687fc9124ead41421efb5c366df18c49728d')

#asyncio.run(main())

print (haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, "K2kseVsmQFgkd15gKkJ+aq9g8Hrpv4zrBylaoZ2nbC0="))
print (haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, "K2kseVsmQFgkd15gKkJ+ao+IN30u9WA8apvZ8LuQYkrUGEcxIhN1tkDM7wnn3V+5"))
print (haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, "K2kseVsmQFgkd15gKkJ+akRXrm2rweXcLkCrwpCecFY="))
print (haphilipsjs.cbc_decode(haphilipsjs.AUTH_SHARED_KEY, ""))
