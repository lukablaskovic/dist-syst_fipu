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
        async with aiosqlite.connect("blicevi/21.11/blicevi.db") as db:
            match received_activity_type:
                case "user":
                    print("user")
                    users.append(data)
                    if len(jokes) > 0:
                        await db.execute("INSERT INTO db (name,city,username,setup,punchline) VALUES (?,?,?,?,?)", 
                            (users[0]["data"]["user"]["name"], 
                            users[0]["user"]["user"]["city"],
                            users["user"]["username"],
                            jokes[0]["jokes"]["setup"],
                            jokes[0]["jokes"]["punchline"]))
                        users = []
                        jokes = []
                        db.commit()
                        await db.execute("SELECT * FROM db")
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