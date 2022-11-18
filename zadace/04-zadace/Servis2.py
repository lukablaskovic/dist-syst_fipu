"""
Servis 2
Drugi servis se sastoji od jedne rute. (/parseActivities)
Unutar drugog servisa aktivnosti se filtriraju ovisno o type, te se zatim
prosljeđuju trećem servisu. 
Charity i Recreational se šalju na posebnu
rutu trećeg servisa (/charityAndRecreational), ostale se šalju na običnu
rutu (/otherActivities).
"""
import aiohttp
import asyncio
import time

from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/parseActivities")
async def parseActivities(req):
    try:
        received_activity = []
        json_data = await req.json()
        received_activity = json_data
        received_activity_type = received_activity.get("type")

        #Filter and group activities by type and send requests to Service3
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            match received_activity_type:

                case "recreational" | "charity":
                    print("recreational|charity: ", received_activity)
                    async with session.post("http://0.0.0.0:8085/charity-recreational", json = received_activity) as resp:
                        service3_res = await resp.text()
                case _:
                    print("other: ", received_activity)
                    async with session.post("http://0.0.0.0:8085/other-activities", json = received_activity) as resp:
                        service3_res = await resp.text()

        return web.json_response({"Status S2" : "OK"}, status=200)        
    except Exception as e:
        return web.json_response({"Status S2" : service3_res}, status=500)    

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8083)