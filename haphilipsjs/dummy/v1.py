from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from haphilipsjs.data.v1 import (
    AMBILIGHT,
    CHANNELLISTS,
    CHANNELS_CURRENT,
    CHANNELS,
    SOURCES_CURRENT,
    SOURCES,
    SYSTEM_55PFL6007T,
    VOLUME,
)


async def put_ambilight_cached(req):
    print("cached")
    return web.json_response({})


async def put_ambilight_mode(req):
    print("mode")
    return web.json_response({})


def get_data(data):
    async def get(req: Request):
        return web.json_response(data)

    return get


app = web.Application()
app.add_routes(
    [
        web.get("/1/system", get_data(SYSTEM_55PFL6007T)),
        web.get("/1/sources", get_data(SOURCES)),
        web.get("/1/sources/current", get_data(SOURCES_CURRENT)),
        web.get("/1/channels", get_data(CHANNELS)),
        web.get("/1/channels/current", get_data(CHANNELS_CURRENT)),
        web.get("/1/audio/volume", get_data(VOLUME)),
        web.get("/1/channellists", get_data(CHANNELLISTS)),
        web.get("/1/ambilight/mode", get_data(AMBILIGHT["mode"])),
        web.post("/1/ambilight/mode", put_ambilight_mode),
        web.get("/1/ambilight/topology", get_data(AMBILIGHT["topology"])),
        web.get("/1/ambilight/measured", get_data(AMBILIGHT["measured"])),
        web.get("/1/ambilight/processed", get_data(AMBILIGHT["processed"])),
        web.get("/1/ambilight/cached", get_data(AMBILIGHT["cached"])),
        web.post("/1/ambilight/cached", put_ambilight_cached),
    ]
)

if __name__ == "__main__":
    web.run_app(app, port=1925)
