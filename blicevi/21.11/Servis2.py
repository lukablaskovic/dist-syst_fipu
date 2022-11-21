import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()
@routes.post("/filterUser")
async def filterUser(req):
    try:
        received_user = []
        json_data = await req.json()
        received_user = json_data

        first_name = received_user["results"][0]["name"]["first"]
        last_name = received_user["results"][0]["name"]["first"]
        city = received_user["results"][0]["city"]
        username = received_user["results"][0]["login"]["username"]

        new_json = {"data" : {"user" : {"name" : first_name + " " + last_name, "city" : city, "username" : username}}}
        print("user:", new_json)
        
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post("http://0.0.0.0:8085/storeData", json = new_json) as resp:
                service4_res = await resp.text()

        return web.json_response({"Status S2" : "OK"}, status=200)
    except Exception as e:
        return web.json_response({"Status S2" : str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)