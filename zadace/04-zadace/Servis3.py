"""
Servis 3
Charity i Recreational se šalju na posebnu
rutu trećeg servisa (/charityAndRecreational), ostale se šalju na običnu
rutu (/otherActivities).
Treći servis sprema svaku aktivnost i tip u
temporary storage. Ukoliko se radi o ruti /otherActivities, za svaku
aktivnost šalje zahtjev na https://randomuser.me/api/ od kojeg uzme
ime, prezime i datum rođenja te pridoda ih kao nove ključeve aktivnosti.
"""

import aiohttp
import asyncio
import time

from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/charityAndRecreational")
async def parseCharRec(req):
    pass

@routes.post("/otherActivities")
async def parseOther(req):
    json_data = await req.json()
    print(json_data)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            task = asyncio.create_task(sendRequest(json_data, session))
            users = await task
            print(users)
    pass

#Send request to randomuser.me api
async def sendRequest(activities, session):
    random_users = []
    for a in range(len(activities)):
        random_users.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
        print("ran - req sent! - ", a)
    res = await asyncio.gather(*random_users)
    res = [await x.json() for x in res]
    return res

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8085)