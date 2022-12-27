import aiohttp

import asyncio
from aiohttp import web

routes = web.RouteTableDef()

print("WT1 running...")


@ routes.post("/process-data")
async def processData(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            record = await req.json()
            response = ""
            if record["username"].lower().startswith('w'):
                print("Found username starting with 'w' ✅")
                response = await sendToM4(record)
            return web.json_response({"WT1": "OK", "response": response}, status=200)
    except Exception as e:
        return web.json_response({"WT1": str(e)}, status=500)


# Send requests to M4.py
async def sendToM4(data):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.post("http://0.0.0.0:1200/gatherData", json=data) as resp:
            m4_resp = await resp.text()
    return m4_resp

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1101)
