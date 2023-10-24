import curses
import platform
import json
import sys
import pprint

from . import PhilipsTV
import asyncio
from ast import literal_eval

pp = pprint.PrettyPrinter(indent=2)

async def monitor_run(stdscr: curses.window, tv: PhilipsTV):

    stdscr.clear()
    stdscr.timeout(1000)

    await tv.update()

    def get_application_name():

        if tv.applications:
            for app in tv.applications.values():
                if app.get("intent") == tv.application:
                    return app.get("label")

        if tv.application:
            return tv.application.get("component", {}).get("className")

    while True:

        stdscr.clear()
        stdscr.addstr(0, 0, "Source")
        if tv.source_id:
            stdscr.addstr(1, 0, await tv.getSourceName(tv.source_id) or "")

        stdscr.addstr(3, 15, "Menu Version")
        if tv.channel_id:
            stdscr.addstr(4, 15, str(tv.settings_version))

        stdscr.addstr(0, 15, "Channel")
        if tv.channel_id:
            stdscr.addstr(1, 15, await tv.getChannelName(tv.channel_id) or "")


        stdscr.addstr(0, 30, "Application")
        if tv.application:
            stdscr.addstr(1, 30, get_application_name() or "")

        stdscr.addstr(0, 45, "Context")
        if tv.context:
            stdscr.addstr(1, 45, tv.context.get("level1", ""))
            stdscr.addstr(2, 45, tv.context.get("level2", ""))
            stdscr.addstr(3, 45, tv.context.get("level3", ""))
            stdscr.addstr(4, 45, tv.context.get("data", ""))


        stdscr.addstr(0, 70, "Channels")
        for idx, channel  in enumerate(tv.channels_current):
            stdscr.addstr(1+idx, 70, str(channel.get("name", channel.get("ccid", ""))))


        def print_pixels(side, offset_y, offset_x):
            stdscr.addstr(offset_y, offset_x, "{}".format(side))
            stdscr.addstr(offset_y + 1, offset_x, "-----------")
            if side not in layer:
                return
            for pixel, data in layer[side].items():
                stdscr.addstr(
                    offset_y + 2 + int(pixel),
                    offset_x,
                    "{:>3} {:>3} {:>3}".format(data["r"], data["g"], data["b"]),
                )

        ambilight = await tv.getAmbilightProcessed()
        if ambilight:
            for idx, layer in enumerate(ambilight.values()):
                offset_y = 6 + 6 * idx
                print_pixels("left", offset_y, 0)
                print_pixels("top", offset_y, 15)
                print_pixels("right", offset_y, 30)
                print_pixels("bottom", offset_y, 45)

        stdscr.refresh()
        if not await tv.notifyChange():
            await tv.update()

        key = stdscr.getch()

        if key == ord("q"):
            break


async def monitor(tv):

    try:
        stdscr = curses.initscr()

        curses.noecho()
        curses.cbreak()

        stdscr.keypad(True)

        try:
            curses.start_color()
        except:
            pass

        return await monitor_run(stdscr, tv)
    finally:
        # Set everything back to normal
        if "stdscr" in locals():
            stdscr.keypad(False)  # type: ignore
            curses.echo()
            curses.nocbreak()
            curses.endwin()

    curses.wrapper(monitor_run, tv)


async def main():
    import argparse
    import logging
    import haphilipsjs
    import ast

    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(prog="python -m haphilipsjs")
    parser.add_argument(
        "-d",
        "--debug",
        help="Debug output",
        dest="debug",
        action="store_true",
        default=False,
    )
    parser.add_argument("-i", "--host", dest="host", required=True)
    parser.add_argument("-a", "--api", dest="api", required=True)
    parser.add_argument(
        "-s",
        "--secured_transport",
        dest="secured_transport",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-u", "--username", dest="username", help="Username", required=False
    )
    parser.add_argument(
        "-p", "--password", dest="password", help="Password", required=False
    )

    subparsers = parser.add_subparsers(help="commands", dest="command")

    status = subparsers.add_parser("status", help="Show current tv status")

    mon = subparsers.add_parser("monitor", help="Monitor current tv status")

    ambilight = subparsers.add_parser("ambilight", help="Control ambilight")
    ambilight.add_argument(
        "--ambilight_mode", dest="ambilight_mode", type=str, required=False
    )
    ambilight.add_argument(
        "--ambilight_cached",
        dest="ambilight_cached",
        type=ast.literal_eval,
        required=False,
    )

    pair = subparsers.add_parser("pair", help="Pair with tv")

    get = subparsers.add_parser("get", help="Get data from endpoint")
    get.add_argument("path", help="Sub path to grab from tv")

    post = subparsers.add_parser("post", help="Post data to endpoint")
    post.add_argument("path", help="Sub path to grab from tv")
    post.add_argument("data", help="Json data to post")

    strings = subparsers.add_parser("strings", help="Get translations")
    strings.add_argument("string_ids", help="List of string id to request", nargs="+")
    strings.add_argument("--language", help="Language code to request")
    strings.add_argument("--country", help="Country code to request")
    strings.add_argument("--variant", help="Variant")

    settings = subparsers.add_parser("settings", help="Get setting")

    settings_commands = settings.add_subparsers(help="settings commands", dest="settings_command")
    settings_get = settings_commands.add_parser("get", help="Get current setting")
    settings_get.add_argument("node_id", help="node id to request", type=int)

    settings_structure = settings_commands.add_parser("structure", help="Get settings structure")

    settings_set = settings_commands.add_parser("set", help="Post a settings value")
    settings_set.add_argument("node_id", help="node id to request", type=int)
    settings_set.add_argument("data", help="Json data to post", type=json.loads)

    markdown = subparsers.add_parser("markdown", help="Print markdown for commandline")
    notify = subparsers.add_parser("notify", help="Look at notify changes, use with debug")


    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
    haphilipsjs.TIMEOUT = 60.0
    tv = haphilipsjs.PhilipsTV(
        args.host,
        int(args.api),
        username=args.username,
        password=args.password,
        secured_transport=args.secured_transport,
    )
    try:
        await run(args, parser, tv)
    finally:
        await tv.aclose()


async def run(args, parser, tv: PhilipsTV):
    if args.command == "status":
        await tv.update()

        print("System: {}".format(tv.system))

        # Simulating homeassistant/components/media_player/philips_js.py
        print("Source: {}".format(await tv.getSourceName(tv.source_id)))
        if tv.sources:
            print(
                "Sources: {}".format(
                    ", ".join(
                        [
                            await tv.getSourceName(srcid) or "None"
                            for srcid in tv.sources
                        ]
                    )
                )
            )
        print(
            "Channel: {}: {}".format(
                tv.channel_id, await tv.getChannelName(tv.channel_id)
            )
        )
        if tv.channels:
            print(
                "Channels: {}".format(
                    ", ".join(
                        [
                            await tv.getChannelName(ccid) or "None"
                            for ccid in list(tv.channels.keys())
                        ]
                    )
                )
            )
        print("Context: {}".format(tv.context))

        print("Application:")
        pp.pprint(tv.application)

        print("Applications:")
        pp.pprint(list(tv.applications.values()))

        print("Power State: {}".format(tv.powerstate))
        print("Screen State: {}".format(tv.screenstate))

        await tv.getAmbilightPower()
        print("Ambilight power: {}".format(tv.ambilight_power))
        print("Ambilight mode: {}".format(tv.ambilight_mode))
        print("Ambilight topology:")
        pp.pprint(await tv.getAmbilightTopology())
        print("Ambilight processed:")
        pp.pprint(await tv.getAmbilightProcessed())
        print("Ambilight measured:")
        pp.pprint(await tv.getAmbilightMeasured())
        print("Ambilight styles:")
        pp.pprint(list(tv.ambilight_styles.values()))
        print("Ambilight currentconfiguration:")
        pp.pprint(tv.ambilight_current_configuration)
        print("Ambilight+Hue State: {}".format(tv.huelamp_power))

    elif args.command == "ambilight":
        if args.ambilight_mode:
            if not await tv.setAmbilightMode(args.ambilight_mode):
                print("Failed to set mode")

        if args.ambilight_cached:
            if not await tv.setAmbilightCached(args.ambilight_cached):
                print("Failed to set ambilight cached")

    elif args.command == "monitor":
        await monitor(tv)

    elif args.command == "pair":
        await tv.getSystem()
        await tv.setTransport(tv.secured_transport, tv.api_version_detected)
        state = await tv.pairRequest(
            "ha-philipsjs", "ha-philipsjs", platform.node(), platform.system(), "native"
        )

        pin = input("Please enter pin displayed on screen: ")

        res = await tv.pairGrant(state, pin)

        print(f"Username: {res[0]}")
        print(f"Password: {res[1]}")

    elif args.command == "get":
        res = await tv.getReq(args.path)
        json.dump(res, sys.stdout, indent=2, ensure_ascii=False)

    elif args.command == "post":
        res = await tv.postReq(args.path, literal_eval(args.data))
        json.dump(res, sys.stdout, indent=2, ensure_ascii=False)

    elif args.command == "strings":
        res = await tv.getStrings(args.string_ids, args.language, args.country, args.variant)
        json.dump(res, sys.stdout, indent=2, ensure_ascii=False)

    elif args.command == "settings":
        if args.settings_command == "structure":
            res = await tv.getMenuItemsSettingsStructure(force=True)
            json.dump(res, sys.stdout, indent=2, ensure_ascii=False)
        elif args.settings_command == "get":
            res = await tv.getMenuItemsSettingsCurrentValue([args.node_id], force=True)
            json.dump(res[args.node_id], sys.stdout, indent=2, ensure_ascii=False)
            print()
        elif args.settings_command == "set":
            res = await tv.postMenuItemsSettingsUpdateData({args.node_id: args.data}, force=True)
            json.dump(res, sys.stdout, indent=2, ensure_ascii=False)
            print()
    elif args.command == "markdown":
        try:
            import argmark  # type: ignore
        except ImportError:
            print("Unable to find argmmark")
            return

        argmark.md_help(parser)

    elif args.command == "notify":
        await tv.update()
        while await tv.notifyChange() is not None:
            pass

if __name__ == "__main__":
    asyncio.run(main())
