from git import Repo
import aiohttp
import asyncio

from aiohttp import web

routes = web.RouteTableDef()

print("M1 running...")


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
            dict_data = [{'id': row[0], 'username': row[1],  'ghlink': row[2],
                          'filename': row[3], 'content': await fetch_repository(row[4])} for row in response_data["response"]]

            for element in dict_data:
                print("content: ", element["content"])

            w1_resp = await send_to_wt("http://wt1:1101/process-data", dict_data)
            w2_resp = await send_to_wt("http://wt2:1102/process-data", dict_data)

            return web.json_response({"M1": "OK", "response": [w1_resp, w2_resp]}, status=200)
    except Exception as e:
        return web.json_response({"M1": str(e)}, status=500)

app = web.Application()


async def fetch_repository(repo):
    repository = Repo.clone_from(repo, "repo")
    content = await repository.git.fetch()
    return content


async def send_to_wt(url, data):
    for i in range(len(data)):
        print("Sending data [{i}] to WT ✔️".format(i=i))
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(url, json=data[i]) as resp:
                wt_resp = await resp.text()

    return wt_resp

app.router.add_routes(routes)

web.run_app(app, port=1001)
