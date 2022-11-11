import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()
temp_storage = []

@routes.get("/fact")
async def get_fact(request):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            facts = []
            for _ in range(20):
                facts.append(asyncio.create_task(session.get("https://catfact.ninja/fact")))
            res = await asyncio.gather(*facts)

            res = [await x.json() for x in res]

            
            tasks = []
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                for i in range(len(res)):
                    tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8080/saveFact")))
                    
            return web.json_response({"status" : "OK"}, status=200)

    except Exception as e:
        return web.json_response({"status" : "failed", "message" : str(e)}, status=500)

temp = []

@routes.post("/saveFact")
async def save_fact(request):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            json_data = await request.json()
            if json_data.get("length") > 100:
                temp.append(json_data)
                return web.json_response({"status" : "OK", "message": json_data.get_fact()}, status=200)

            else:
                return web.json_response({"status" : "failed", "message" : str(e)}, status=400)
    except Exception as e:
        return web.json_response({"status" : "failed", "message" : str(e)}, status=500)



app = web.Application()

app.router.add_routes(routes)

web.run_app(app)