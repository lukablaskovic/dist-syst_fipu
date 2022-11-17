"""
Servis 1
________
Kreiraj tri web servisa. Prvi se sastoji od jedne rute. (/getActivity) Unutar 30 sekundi šalje pet puta po 8 zahtjeva na https://www.boredapi.com
/api/activity. Rezultate prosljeđuje pojedinačno prosljeđuje drugom servisu.
"""
import aiohttp
import asyncio
import time

from aiohttp import web
import json

routes = web.RouteTableDef()
activities = []

@routes.get("/getActivity")
async def get_activity(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            activites = []
            t_end = time.time() + 30
            while time.time() < t_end:
                print("Starting...")
                for r in range(8):
                    activities.append(asyncio.create_task(session.get("https://www.boredapi.com/api/activity")))
                    print("Sending request - ", r)
                res = await asyncio.gather(*activities)
                res = [await x.json() for x in res]
                time.sleep(6)
            print(activites)
        return web.json_response({"status" : "OK", "message" : res}, status=200)
    except Exception as e:
        return web.json_response({"failed" : str(e)}, status=500) 

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)