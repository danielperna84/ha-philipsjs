if __name__ == '__main__':
    import argparse
    import logging
    import haphilipsjs

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
    args = parser.parse_args()
    logging.basicConfig(level=args.debug and logging.DEBUG or logging.INFO)
    haphilipsjs.TIMEOUT = 60.0
    tv = haphilipsjs.PhilipsTV(args.host, int(args.api))
    tv.update()
    tv.getChannelId()
    tv.getChannels()

    # Simulating homeassistant/components/media_player/philips_js.py
    logger.info('Source: %s', tv.getSourceName(tv.source_id))
    if tv.sources:
        logger.info(
            'Sources: %si...',
            ', '.join([
                tv.getSourceName(srcid)
                for srcid in tv.sources
            ])
        )
    logger.info('Channel: %s', tv.getChannelName(tv.channel_id))
    if tv.channels:
        logger.info(
            'Channels: %s...',
            ', '.join([
                tv.getChannelName(ccid)
                for ccid in list(tv.channels.keys())[:10]
            ])
        )
