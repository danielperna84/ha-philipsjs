import curses
import platform
from . import PhilipsTV

def monitor_run(stdscr, tv: PhilipsTV):

    stdscr.clear()
    stdscr.timeout(1000)

    tv.update()

    def get_application_name():

        if tv.applications:
            for app in tv.applications["applications"]:
                if app["intent"] == tv.application:
                    return app["label"]

        return f"{tv.application['component']['className']}"

    while True:

        stdscr.clear()
        stdscr.addstr(0, 0, "Source")
        if tv.source_id:
            stdscr.addstr(1, 0, tv.getSourceName(tv.source_id))

        stdscr.addstr(0, 15, "Channel")
        if tv.channel_id:
            stdscr.addstr(1, 15, tv.getChannelName(tv.channel_id))

        stdscr.addstr(0, 30, "Application")
        if tv.application:
            stdscr.addstr(1, 30, get_application_name())

        stdscr.addstr(0, 45, "Context")
        if tv.context:
            stdscr.addstr(1, 45, tv.context.get("level1", ""))
            stdscr.addstr(2, 45, tv.context.get("level2", ""))
            stdscr.addstr(3, 45, tv.context.get("level3", ""))
            stdscr.addstr(3, 45, tv.context.get("data", ""))

        def print_pixels(side, offset_y, offset_x):
            stdscr.addstr(offset_y, offset_x, "{}".format(side))
            stdscr.addstr(offset_y+1, offset_x, "-----------")
            if side not in layer:
                return
            for pixel, data in layer[side].items():
                stdscr.addstr(
                    offset_y+2+int(pixel),
                    offset_x, 
                    "{:>3} {:>3} {:>3}".format(data["r"], data["g"], data["b"])
                )

        ambilight = tv.getAmbilightProcessed()
        if ambilight:
            for idx, layer in enumerate(ambilight.values()):
                offset_y = 6 + 6*idx
                print_pixels("left", offset_y, 0)
                print_pixels("top", offset_y, 15)
                print_pixels("right", offset_y, 30)
                print_pixels("bottom", offset_y, 45)

        stdscr.refresh()
        tv.update()
        key = stdscr.getch()
        
        if key == ord("q"):
            break

def monitor(tv):
    curses.wrapper(monitor_run, tv)

if __name__ == '__main__':
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
    parser.add_argument("-u", "--username", dest="username", help="Username", required=False)
    parser.add_argument("-p", "--password", dest="password", help="Password", required=False)

    subparsers = parser.add_subparsers(help='commands', dest="command")

    status = subparsers.add_parser("status", help="Show current tv status")

    mon = subparsers.add_parser("monitor", help="Monitor current tv status")

    ambilight = subparsers.add_parser("ambilight", help="Control ambilight")
    ambilight.add_argument("--ambilight_mode", dest="ambilight_mode", type=str, required=False)
    ambilight.add_argument("--ambilight_cached", dest="ambilight_cached", type=ast.literal_eval, required=False)

    pair = subparsers.add_parser("pair", help="Pair with tv")

    markdown = subparsers.add_parser("markdown", help="Print markdown for commandline")

    args = parser.parse_args()
    logging.basicConfig(level=args.debug and logging.DEBUG or logging.INFO)
    haphilipsjs.TIMEOUT = 60.0
    tv = haphilipsjs.PhilipsTV(args.host, int(args.api), username=args.username, password=args.password)

    if args.command == "status":
        tv.update()
        tv.getChannelId()
        tv.getChannels()

        # Simulating homeassistant/components/media_player/philips_js.py
        print('Source: {}'.format(tv.getSourceName(tv.source_id)))
        if tv.sources:
            print(
                'Sources: {}'.format(
                ', '.join([
                    tv.getSourceName(srcid) or "None"
                    for srcid in tv.sources
                ]))
            )
        print('Channel: {}: {}'.format(tv.channel_id, tv.getChannelName(tv.channel_id)))
        if tv.channels:
            print(
                'Channels: {}'.format(
                ', '.join([
                    tv.getChannelName(ccid) or "None"
                    for ccid in list(tv.channels.keys())
                ]))
            )
        print('Context: {}'.format(tv.context))

        print('Ambilight mode: {}'.format(tv.getAmbilightMode()))
        print('Ambilight topology: {}'.format(tv.getAmbilightTopology()))
        print('Ambilight processed: {}'.format(tv.getAmbilightProcessed()))
        print('Ambilight measured: {}'.format(tv.getAmbilightMeasured()))


    elif args.command == "ambilight":
        if args.ambilight_mode:
            if not tv.setAmbilightMode(args.ambilight_mode):
                print("Failed to set mode")

        if args.ambilight_cached:
            if not tv.setAmbilightCached(args.ambilight_cached):
                print("Failed to set ambilight cached")

    elif args.command == "monitor":
        monitor(tv)


    elif args.command == "pair":
        tv.getSystem()
        tv.setTransport(tv.secured_transport, tv.api_version_detected)
        state = tv.pairRequest("ha-philipsjs", "ha-philipsjs", platform.node(), platform.system(), "native")

        pin = input("Please enter pin displayed on scree")

        res = tv.pairGrant(state, pin)

        print(f"Username: {res[0]}")
        print(f"Password: {res[1]}")

    elif args.command == "markdown":
        import argmark
        argmark.md_help(parser)
