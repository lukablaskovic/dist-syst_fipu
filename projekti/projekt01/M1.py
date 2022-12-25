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
            data.append(asyncio.create_task(
                session.get("ttp://0.0.0.0:1000/github-links")))
            res = await asyncio.gather(*data)
            response_data = await res[0].json()

            dict_data = [{'id': l[0], 'username': l[1],  'ghlink': l[2],
                          'filename': l[3]} for l in response_data["payload"]]

            usernames_w = [
                element for element in dict_data if element["username"].lower().startswith('w')]
            usernames_d = [
                element for element in dict_data if element["username"].lower().startswith('d')]

            print("username_w: ", usernames_w)
            print("username_d:", usernames_d)

            return web.json_response({"M1": "OK"}, status=200)
    except Exception as e:
        return web.json_response({"M1": str(e)}, status=500)

app = web.Application()


# Send request to M0, receive 100 random rows
async def sendRequests(data, session):
    data.append(asyncio.create_task(
        session.get("ttp://0.0.0.0:1000/github-links")))
    return data

app.router.add_routes(routes)

web.run_app(app, port=1001)
