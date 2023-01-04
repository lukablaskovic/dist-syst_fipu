from git import Repo
import git.exc as ge
import aiohttp
import asyncio
import os
import shutil

from aiohttp import web

routes = web.RouteTableDef()

print("M1 running...")


# M1 start route
# Call using http://localhost:1000/start
@ routes.get("/start")
async def fetchData(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = []
            # Send request to M0, receive 100 random rows
            data.append(asyncio.create_task(
                session.get("http://m0:1000/github-links")))
            res = await asyncio.gather(*data)
            response_data = await res[0].json()

            dict_data = [{'id': row[0], 'username': row[1],  'ghlink': row[2],
                          'filename': row[3], 'content': row[2]} for row in response_data["response"]]
            w1_resp = await send_to_wt("http://wt1:1101/process-data", dict_data)
            w2_resp = await send_to_wt("http://wt2:1102/process-data", dict_data)

            return web.json_response({"M1": "OK", "response": [w1_resp, w2_resp]}, status=200)
    except Exception as e:
        return web.json_response({"M1": str(e)}, status=500)


# M1+, fetching content from repositories using GitPython. It works, but it's very slow
@ routes.get("/start2")
async def fetchData2(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = []
            # Send request to M0, receive 100 random rows
            data.append(asyncio.create_task(
                session.get("http://m0:1000/github-links")))
            res = await asyncio.gather(*data)
            response_data = await res[0].json()
            content = []
            # Fetch repositories contents concurrently
            for row in response_data["response"]:
                task = asyncio.create_task(fetch_repository(row[2], row[3]))
                content.append(task)
            results = await asyncio.gather(*content)
            dict_data = [{'id': row[0], 'username': row[1],  'ghlink': row[2],
                          'filename': row[3], 'content': result} for row, result in zip(response_data["response"], results)]

            print("All repository contents successfully retrieved! ✅")
            w1_resp = await send_to_wt("http://wt1:1101/process-data", dict_data)
            w2_resp = await send_to_wt("http://wt2:1102/process-data", dict_data)

            return web.json_response({"M1": "OK", "response": [w1_resp, w2_resp]}, status=200)
    except Exception as e:
        return web.json_response({"M1": str(e)}, status=500)


app = web.Application()


# Fetch content from repositories
async def fetch_repository(repo, filename):
    # Clone repository and delete local repo folder on startup if exists
    if os.path.exists("repo"):
        shutil.rmtree("repo")
    repository = Repo.clone_from(repo, "repo")

    commit = repository.commit("HEAD")
    tree = commit.tree

    # Find the blob object for the file specified using BFS
    # Sporo je ali radi, nisam znao kako napraviti brže...
    # Koristi breadth-first search za pretraživanje stabla kod pronalaska točog .py file-a
    queue = [(tree, filename)]
    while queue:
        item, name = queue.pop(0)
        if item.type == "blob" and item.name == name:
            blob = item
            break
        elif item.type == "tree":
            for child in item.traverse():
                queue.append((child, name))
    else:
        blob = None

    # Retrieve content
    if blob:
        content = repository.git.show("{}:{}".format(commit.hexsha, blob.path))
        print("Content successfuly retrieved! ✅")
    return content


# Send data to WT services
async def send_to_wt(url, data):
    for i in range(len(data)):
        print("Sending data [{i}] to WT ✔️".format(i=i))
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(url, json=data[i]) as resp:
                wt_resp = await resp.text()

    return wt_resp

app.router.add_routes(routes)

web.run_app(app, port=1001)
