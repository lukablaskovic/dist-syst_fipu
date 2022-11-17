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
received_activities = []

charity = []
recreational = []
other = []

@routes.post("/parseActivities")
async def parseActivities(req):
    try:
        json_data = await req.json()
        received_activities.append(json_data)
        
        charity = [activity for activity in received_activities if activity["type"] == "charity"]
        recreational = [activity for activity in received_activities if activity["type"] == "recreational"]
        other = [activity for activity in received_activities if activity["type"] != "recreational" and activity["type"] != "charity"]

        print("charity:", charity)

        print("recreational:", recreational)

        print("other:", other)

        return web.json_response({"status" : "OK"}, status=200)        
    except Exception as e:
        return web.json_response({"failed" : str(e)}, status=500)         

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8083)