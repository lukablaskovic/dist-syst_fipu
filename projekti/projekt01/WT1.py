import aiohttp
import aiosqlite
import asyncio

from aiohttp import web

routes = web.RouteTableDef()


@ routes.post("/process-data")
async def processData(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = await req.json()
            usernames_w = [
                element for element in data if element["username"].lower().startswith('w')]
            print(usernames_w)
            return web.json_response({"WT1": "OK"}, status=200)
    except Exception as e:
        return web.json_response({"WT1": str(e)}, status=500)

# Send requests to M4.py


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1101)
