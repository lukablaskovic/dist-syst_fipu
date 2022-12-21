import aiohttp
import aiosqlite
import asyncio

from aiohttp import web

routes = web.RouteTableDef()

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1000)
