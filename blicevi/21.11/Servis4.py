import aiohttp
import asyncio
import aiosqlite
from aiohttp import web

routes = web.RouteTableDef()



@routes.post("/storeData")
async def storeData(request):
    users = []
    jokes = []
    data = await request.json()
    print(data)
    received_activity_type = data["data"].keys()

    try:
        async with aiosqlite.connect("activities.db") as db:
            match received_activity_type:
                case "user":
                    print("user")
                    users.append(data)
                case "joke":
                    print("joke")
                    jokes.append(data)
        await db.commit()


        print("Succesfully inserted!")
        return web.json_response({"status": "Successfuly inserted data"}, status=200)
    except Exception as e:
        return web.json_response({"Status S2" : str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8085)