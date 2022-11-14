import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

temp = [
    {
        "ime" : "Stol"
    },
    {
        "ime" : "Laptop"
    }
]

@routes.get("/")
async def get_handler(request):
    try:
        tasks = []
        async with aiohttp.ClientSession() as session:
            for _ in range(5):
                tasks.append(asyncio.create_task(session.get(session.get("https://google.com"))))
            res = await asyncio.gather(*tasks)
            res = [await x.json() for x in res]
            res = [len(await x.text) for x in res]
            print(res)

    except Exception as e:
        return web.json_response({"status" : "failed", "message" : str(e)}, status=500)
    return web.json_response({"status" : "OK"}, status=200)

@routes.get("/artikl")
async def get_artikl(request):
    print(request)
    data = request.query
    data = data.get("ime")

    q = request.query.get("ime")
    res = [d for d in temp if d.get("ime") == q]


    print(data)
    return web.json_response({"status" : "OK", "data" : res}, status=200)



@routes.post("/artikl")
async def post_artikl(request):
    json_data = await request.json()
    print(json_data)
    temp.append(json_data)
    return web.json_response({"status" : "OK"}, status=200)




app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
