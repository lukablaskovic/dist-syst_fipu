import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()
@routes.get("/getJokes")
async def getJokes(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for c in range(6):
                print("Cycle {} starting...".format(c+1))

                json_data = []
                activities = []

                #Send 8 requests and gather results
                task1 = asyncio.create_task(sendRequests1(activities, session))
                #SERVICE2
                activities1 = await task1
                res = await asyncio.gather(*activities1)
                json_data = [await x.json(content_type=None) for x in res]
                #Send json_data to parser1
                task1 = asyncio.create_task(sendToParser1(json_data, session))
                service2_response = await task1

                json_data = []
                activities = []

                #SERVICE3
                task2 = asyncio.create_task(sendRequests2(activities, session))
                activities2 = await task2
                res = await asyncio.gather(*activities2)
                json_data2 = [await x.json(content_type=None) for x in res]
                #Send json_data to parser2
                task2 = asyncio.create_task(sendToParser2(json_data2, session))
                service3_response = await task2
                
        return web.json_response({"Status S1" : "OK"}, status=200)
    except Exception as e:
        return web.json_response({"Status S1" : str(e)}, status=500)

#Send requests1
async def sendRequests1(activities, session):
    for a in range(2):
        activities.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
        print("Sending request1 - ", a+1)
    return activities

#Send requests2
async def sendRequests2(activities, session):
    for a in range(2):
        activities.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
        print("Sending request2 - ", a)
    return activities

#Send requests to Service2 parser
async def sendToParser1(json_activities, session):
    for i in range(len(json_activities)):
        async with session.post("http://0.0.0.0:8082/filterUser", json=json_activities[i]) as resp:
            print("Sending to parser - ", i)
            service2_response = await resp.text()
    return service2_response


#Send requests to Service2 parser
async def sendToParser2(json_activities, session):
    for i in range(len(json_activities)):
        async with session.post("http://0.0.0.0:8083/filterJoke", json=json_activities[i]) as resp:
            print("Sending to parser - ", i)
            service3_response = await resp.text()
    return service3_response

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)