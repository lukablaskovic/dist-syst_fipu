import aiohttp
import aiosqlite
import asyncio
import time

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getActivity")
async def getActivity(req):
    try:
        t_end = time.time() + 30
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            while time.time() < t_end:
                print("Starting...")
                #Šalji zahtjeve 5 puta
                for c in range(5):
                    print("Cycle {} starting...".format(c+1))

                    json_data = []
                    activities = []

                    #Send 8 requests and gather results
                    task = asyncio.create_task(sendRequests(activities, session))
                    activities = await task
                    res = await asyncio.gather(*activities)
                    json_data = [await x.json() for x in res]
                    print(json_data)
                    
                    task = asyncio.create_task(saveActivities(json_data, session))
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
        print("Sending request - ", a)
    return activities

#Send requests to Service2 parser
async def saveActivities(json_activities, session):
    for i in range(len(json_activities)):
        async with session.post("http://0.0.0.0:8082/saveActivity", json=json_activities[i]) as resp:
            print("Sending... - ", i)
            service2_response = await resp.text()
    return service2_response

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8085)