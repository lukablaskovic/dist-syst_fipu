import aiohttp
import aiosqlite
import asyncio
import aiofiles
from aiohttp import web

routes = web.RouteTableDef()

received_code = []


@ routes.post("/gatherData")
async def gatherData(req):
    try:
        code = await req.json()
        print("Code received and stored! ✅")
        received_code.append(code)
        return web.json_response({"M41": "OK"}, status=200)
    except Exception as e:
        return web.json_response({"M41": str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1200)
