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

temp_activities_storage = []

@routes.post("/charity-recreational")
async def parseCharRec(req):
    try:
        json_data = await req.json()
        print("ROUTE: charity-recreational")
        new_activity = json_data
        temp_activities_storage.append(new_activity)
        
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                task = asyncio.create_task(sendRequest(session))
                user_json = await task
                new_activity["latitude"] = user_json["results"][0]["location"]["coordinates"]["latitude"]
                new_activity["longitude"] = user_json["results"][0]["location"]["coordinates"]["longitude"]
                print(new_activity)
                
        return web.json_response({"status" : "success"}, status=200)
    except Exception as e:
        web.json_response({"failed" : str(e)}, status = 500)

@routes.post("/other-activities")
async def parseOther(req):
    try:
        json_data = await req.json()
        print("ROUTE: other-activities")
        new_activity = json_data
        temp_activities_storage.append(new_activity)
        
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                task = asyncio.create_task(sendRequest(session))
                user_json = await task
                new_activity["ime"] = user_json["results"][0]["name"]["first"]
                new_activity["prezime"] = user_json["results"][0]["name"]["last"]
                new_activity["datum_rodenja"] = user_json["results"][0]["dob"]["date"][:10]
                print(new_activity)
                
        return web.json_response({"Status S3" : "OK"}, status=200)
    except Exception as e:
        web.json_response({"Status S3" : str(e)}, status = 500)


#Send request to randomuser.me api
async def sendRequest(session):
    random_user = asyncio.create_task(session.get("https://randomuser.me/api/"))
    res = await random_user
    user_json = await res.json()
    return user_json

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8085)