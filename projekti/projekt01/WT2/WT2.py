import aiohttp

import asyncio
from aiohttp import web

routes = web.RouteTableDef()

print("WT2 running...")


@ routes.post("/process-data")
async def processData(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            record = await req.json()
            response = ""
            if record["username"].lower().startswith('d'):
                print("Found username starting with 'd' ✅")
                response = await sendToM4(record)
            return web.json_response({"WT2": "OK", "response": response}, status=200)
    except Exception as e:
        return web.json_response({"WT2": str(e)}, status=500)


# Send requests to M4.py
async def sendToM4(data):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.post("http://m4:1200/gatherData", json=data) as resp:
            m4_resp = await resp.text()
    return m4_resp

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1102)
