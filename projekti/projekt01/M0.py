import aiohttp
import aiosqlite
import asyncio

import pandas as pd


from aiohttp import web

routes = web.RouteTableDef()


@ routes.get("/github-links")
async def getGithubLinks(req):
    try:
        async with aiosqlite.connect("projekti/projekt01/data.db") as db:
            # Check if table is empty
            async with db.execute("SELECT COUNT(1) WHERE EXISTS (SELECT * FROM data)") as cur:
                async for row in cur:
                    print(row)
                    await fillDB()
        return web.json_response({"M0": "OK"}, status=200)
    except Exception as e:
        return web.json_response({"M0": str(e)}, status=500)


async def fillDB():
    df = pd.read_json('/Users/lukablaskovic/Desktop/data.json', lines=True)
    async with aiosqlite.connect("projekti/projekt01/data.db") as db:
        for index, row in df.head(10000).iterrows():
            username = row["repo_name"]
            ghlink = "https://github.com/{repository}".format(
                repository=row["repo_name"])
            filename = row["path"].split("/")[-1]
            print(row["repo_name"])
            await db.execute("INSERT INTO data (username, ghlink, filename) VALUES (?,?, ?)", (username, ghlink, filename))
            await db.commit()
    pass

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1000)
