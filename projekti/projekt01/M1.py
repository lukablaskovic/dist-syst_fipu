import aiohttp
import aiosqlite
import asyncio

from aiohttp import web

routes = web.RouteTableDef()


@ routes.get("/data")
async def fetchData(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = []
            # Send request to M0, receive 100 random rows
            data.append(asyncio.create_task(
                session.get("http://0.0.0.0:1000/github-links")))
            res = await asyncio.gather(*data)
            response_data = await res[0].json()
            dict_data = [{'id': l[0], 'username': l[1],  'ghlink': l[2],
                          'filename': l[3], 'content': l[4]} for l in response_data["response"]]
            w1_resp = await send_to_wt("http://0.0.0.0:1101/process-data", dict_data)
            w2_resp = await send_to_wt("http://0.0.0.0:1102/process-data", dict_data)

            return web.json_response({"M1": "OK", "response": [w1_resp, w2_resp]}, status=200)
    except Exception as e:
        return web.json_response({"M1": str(e)}, status=500)

app = web.Application()


async def send_to_wt(url, data):
    for i in range(len(data)):
        print("Sending data [{i}] to WT ✔️".format(i=i))
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(url, json=data[i]) as resp:
                wt_resp = await resp.text()

    return wt_resp

app.router.add_routes(routes)

web.run_app(app, port=1001)
