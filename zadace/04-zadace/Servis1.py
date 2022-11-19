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

routes = web.RouteTableDef()

@routes.get("/getActivity")
async def get_activity(req):
    try:
        t_end = time.time() + 30
    
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            #Radi 30 sekundi
            while time.time() < t_end:
                print("Starting...")
                #Šalji zahtjeve 5 puta
                for c in range(5):
                    print("Cycle {} starting...".format(c+1))

                    #Posalji 8 zahtjeva i spremi ih
                    activities = []
                    #Send 8 requests
                    task = asyncio.create_task(sendRequests(activities, session))
                    #Awaits 8 requests sends to finish
                    activities = await task
                    #Gather and unpack data from task results
                    res = await asyncio.gather(*activities)
                    json_data = [await x.json() for x in res]
                        
                    print(json_data)
                    print("len(res): ", len(json_data))
                        
                    #Send json_data to parser
                    
                    task = asyncio.create_task(sendToParser(json_data, session))
                    service2_response = await task
                    print("Cycle {} finished".format(c+1))
                    time.sleep(6)
                break

        return web.json_response({"Status S1" : "OK"}, status=200)
    except Exception as e:
        return web.json_response({"Status S1" : service2_response}, status=500)

#Send requests to bored api
async def sendRequests(activities, session):
    for a in range(8):
        activities.append(asyncio.create_task(session.get("https://www.boredapi.com/api/activity")))
        #print("Sending request - ", a)
    return activities
        
#Send requests to Service2 parser
async def sendToParser(json_activities, session):
    for i in range(len(json_activities)):
        async with session.post("http://0.0.0.0:8083/parseActivities", json=json_activities[i]) as resp:
            print("Sending to parser - ", i)
            service2_response = await resp.text()
    return service2_response

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)