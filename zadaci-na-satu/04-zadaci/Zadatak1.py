import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/fact")
async def get_fact(request):
    facts = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        for _ in range(20):
            facts.append(asyncio.create_task(session.get("https://catfact.ninja/fact")))
        res = await asyncio.gather(*facts)
        res = [await x.json() for x in res]
    facts = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        for i in range(len(res)):
            facts.append(asyncio.create_task(session.post("http://0.0.0.0:8081/saveFact", json= res[i])))
        res = await asyncio.gather(*facts)
        res = [await x.json() for x in res]
    return web.json_response({"status" : "OK", "message" : res}, status=200)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8080)