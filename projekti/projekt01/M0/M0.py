import aiohttp
import aiosqlite
import asyncio

import pandas as pd
import numpy as np

from aiohttp import web

routes = web.RouteTableDef()

print("M0 running...")


@ routes.get("/github-links")
async def getGithubLinks(req):
    try:
        async with aiosqlite.connect("/app/data.db") as db:
            # SQL Query which checks if table is empty
            # Return: 0 - empty, 1 - not empty
            async with db.execute("SELECT COUNT(1) WHERE EXISTS (SELECT * FROM data)") as cur:
                async for row in cur:
                    if tableIsEmpty(row[0]):
                        print("Database is empty. Filling up... ⚠️")
                        await fillDB()
                        print("Database filled successfuly!")
                        data = await fetchRandomRows(db)
                    else:
                        data = await fetchRandomRows(db)

        return web.json_response({"M0": "OK", "response": data}, status=200)
    except Exception as e:
        return web.json_response({"M0": "ERROR", "response": str(e)}, status=500)


def tableIsEmpty(countResult):
    return True if countResult == 0 else False


async def fetchRandomRows(conn):
    cursor = await conn.cursor()
    # Get the total number of rows in the table
    await cursor.execute("SELECT COUNT(*) FROM data")
    (total_rows,) = await cursor.fetchone()

    # Generate a list of 100 random row indices
    row_indices = np.random.randint(0, total_rows, size=100)
    # Fetch the rows with the randomly selected indices
    rows = []
    for row_index in row_indices:
        await cursor.execute("SELECT * FROM data LIMIT 1 OFFSET {row_index}".format(row_index=row_index))
        rows.append(await cursor.fetchone())
    return rows


async def fillDB():
    try:
        df = pd.read_json('/app/data', lines=True)
        print(df.head())
        async with aiosqlite.connect("/app/data.db") as db:
            for index, row in df.head(10000).iterrows():
                username = row["repo_name"].split("/")[0]
                ghlink = "https://github.com/{repository}".format(
                    repository=row["repo_name"])
                file_name = row["path"].split("/")[-1]
                content = row["content"]

                try:
                    await db.execute("INSERT INTO data (username, ghlink, file_name, content) VALUES (?, ?, ?, ?)", (username, ghlink, file_name, content))
                    await db.commit()
                except Exception as e:
                    print("An error has occured when inserting into database: ", e)
            print("Successfuly added files to database! ✅")
        pass
    except Exception as e:
        return web.json_response({"M0": "ERROR", "response": str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=1000)
