import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()
@routes.post("/filterJoke")
async def filterJoke(req):
    try:
        received_joke = []
        json_data = await req.json()
        received_joke = json_data

        setup = received_joke["setup"]
        punchline = received_joke["punchline"]

        new_json = {"data" : {"joke" : {"setup" : setup, "punchline" : punchline}}}
        print("JOKE:", new_json)
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post("http://0.0.0.0:8085/storeData", json = new_json) as resp:
                service4_res = await resp.text()

        return web.json_response({"Status S2" : "OK"}, status=200)
    except Exception as e:
        return web.json_response({"Status S2" : str(e)}, status=500)

#Send requests1
async def sendRequests1(activities, session):
    for a in range(2):
        activities.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
        print("Sending request1 - ", a)
    return activities

#Send requests2
async def sendRequests2(activities, session):
    for a in range(2):
        activities.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
        print("Sending request2 - ", a)
    return activities

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8083)