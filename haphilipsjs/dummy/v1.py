from aiohttp import web
from aiohttp.web_response import json_response

from haphilipsjs.data.v1 import (
    AMBILIGHT,
    CHANNELLISTS,
    CHANNELS_CURRENT,
    CHANNELS,
    SOURCES_CURRENT,
    SOURCES,
    SYSTEM,
    VOLUME,
)

def put_ambilight_cached(req):
    print("cached")
    return web.json_response({})


def put_ambilight_mode(req):
    print("mode")
    return web.json_response({})

app = web.Application()
app.add_routes([
    web.get('/1/system', lambda req: web.json_response(SYSTEM)),
    web.get('/1/sources', lambda req: web.json_response(SOURCES)),
    web.get('/1/sources/current', lambda req: web.json_response(SOURCES_CURRENT)),
    web.get('/1/channels', lambda req: web.json_response(CHANNELS)),
    web.get('/1/channels/current', lambda req: web.json_response(CHANNELS_CURRENT)),
    web.get('/1/audio/volume', lambda req: web.json_response(VOLUME)),
    web.get('/1/channellists', lambda req: web.json_response(CHANNELLISTS)),
    web.get('/1/ambilight/mode', lambda req: web.json_response(AMBILIGHT["mode"])),
    web.post('/1/ambilight/mode', put_ambilight_mode),
    web.get('/1/ambilight/topology', lambda req: web.json_response(AMBILIGHT["topology"])),
    web.get('/1/ambilight/measured', lambda req: web.json_response(AMBILIGHT["measured"])),
    web.get('/1/ambilight/processed', lambda req: web.json_response(AMBILIGHT["processed"])),
    web.get('/1/ambilight/cached', lambda req: web.json_response(AMBILIGHT["cached"])),
    web.post('/1/ambilight/cached', put_ambilight_cached),
])

if __name__ == '__main__':
    web.run_app(app, port=1925)