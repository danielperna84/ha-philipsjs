import curses
from . import PhilipsTV

def monitor_run(stdscr, tv: PhilipsTV):

    stdscr.clear()

    source_pad = stdscr.subpad(2, 15, 0, 0)
    channel_pad = stdscr.subpad(2, 15, 0, 15)

    ambilight_pad = stdscr.subpad(10, 80, 3, 0)



    while True:
        tv.update()
        stdscr.clear()
        stdscr.addstr(0, 0, "Source")
        if tv.source_id:
            stdscr.addstr(1, 0, tv.getSourceName(tv.source_id))

        stdscr.addstr(0, 15, "Channel")
        if tv.channel_id:
            stdscr.addstr(1, 15, tv.getChannelName(tv.channel_id))

        def print_pixels(side, offset_y, offset_x):
            stdscr.addstr(offset_y, offset_x, "{}".format(side))
            stdscr.addstr(offset_y+1, offset_x, "-----------".format(side))
            for pixel, data in layer[side].items():
                stdscr.addstr(
                    offset_y+2+int(pixel),
                    offset_x, 
                    "{:>3} {:>3} {:>3}".format(data["r"], data["g"], data["b"])
                )

        ambilight = tv.getAmbilightProcessed()
        if ambilight:
            for idx, layer in enumerate(ambilight.values()):
                offset_y = 5 + 6*idx
                print_pixels("left", offset_y, 0)
                print_pixels("top", offset_y, 15)
                print_pixels("right", offset_y, 30)
                print_pixels("bottom", offset_y, 45)

        stdscr.refresh()
        curses.napms(1000)

def monitor(tv):
    curses.wrapper(monitor_run, tv)

if __name__ == '__main__':
    import argparse
    import logging
    import haphilipsjs
    import ast

    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser()
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
    parser.add_argument("-s", "--status", dest="status", help="Print current status", action='store_true')
    parser.add_argument("--ambilight_mode", dest="ambilight_mode", type=str)
    parser.add_argument("--ambilight_cached", dest="ambilight_cached", type=ast.literal_eval)
    parser.add_argument("--monitor", dest="monitor", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(level=args.debug and logging.DEBUG or logging.INFO)
    haphilipsjs.TIMEOUT = 60.0
    tv = haphilipsjs.PhilipsTV(args.host, int(args.api))

    if args.status:
        tv.update()
        tv.getChannelId()
        tv.getChannels()

        # Simulating homeassistant/components/media_player/philips_js.py
        print('Source: {}'.format(tv.getSourceName(tv.source_id)))
        if tv.sources:
            print(
                'Sources: {}'.format(
                ', '.join([
                    tv.getSourceName(srcid)
                    for srcid in tv.sources
                ]))
            )
        print('Channel: {}: {}'.format(tv.channel_id, tv.getChannelName(tv.channel_id)))
        if tv.channels:
            print(
                'Channels: {}'.format(
                ', '.join([
                    tv.getChannelName(ccid)
                    for ccid in list(tv.channels.keys())[:10]
                ]))
            )

        print('Ambilight mode: {}'.format(tv.getAmbilightMode()))
        print('Ambilight topology: {}'.format(tv.getAmbilightTopology()))


    if args.ambilight_mode:
        if not tv.setAmbilightMode(args.ambilight_mode):
            print("Failed to set mode")

    if args.ambilight_cached:
        if not tv.setAmbilightCached(args.ambilight_cached):
            print("Failed to set ambilight cached")

    if args.monitor:
        monitor(tv)