import aiohttp
import aiosqlite
import asyncio

from aiohttp import web

routes = web.RouteTableDef()


@ routes.post("/process-data")
async def processData(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:

            return web.json_response({"WT2": "OK"}, status=200)
    except Exception as e:
        return web.json_response({"WT2": str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1102)
