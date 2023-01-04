
import aiosqlite

import pandas as pd
import numpy as np

from aiohttp import web

from main import add_entry, get_entry

routes = web.RouteTableDef()

print("M0 running...")


@ routes.get("/github-links")
async def getGithubLinks(req):
    try:
        await add_to_blockchain()
        return web.json_response({"M0": "OK", }, status=200)
    except Exception as e:
        return web.json_response({"M0": "ERROR", "response": str(e)}, status=500)


async def add_to_blockchain():
    df = pd.read_json('Route/To/data', lines=True)
    print(df.head())
    try:
        for index, row in df.head(10000).iterrows():
            username = row["repo_name"].split("/")[0]
            ghlink = "https://github.com/{repository}".format(
                repository=row["repo_name"])
            file_name = row["path"].split("/")[-1]
            add_entry(username, ghlink, file_name)
    except Exception as e:
        print("An error has occured when inserting into blockchain: ", e)
        print("Successfuly added files to blockchain! ✅")


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1000)
