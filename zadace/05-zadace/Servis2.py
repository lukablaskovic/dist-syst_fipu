import aiohttp
import asyncio
import time
import aiosqlite


from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/saveActivity")
async def saveActivity(request):
    req = await request.json()
    print(req)
    try:
        async with aiosqlite.connect("activities.db") as db:
            await db.execute("INSERT INTO activities (activity,type,participants,price,link,key,accessibility) VALUES (?,?,?,?,?,?,?)", 
            (req["activity"], req["type"], req["participants"], req["price"], req["link"], req["key"], req["accessibility"]))
            await db.commit()
            print("Succesfully inserted!")
        return web.json_response({"status": "Successfuly inserted data"}, status=200)
    except Exception as e:
        return web.json_response({"Status S2" : str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)