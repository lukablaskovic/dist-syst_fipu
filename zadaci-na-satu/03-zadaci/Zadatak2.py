"""
2. Kreirajte tri asinkrone funkcije te funkciju main. Prva funkcija uzima
listu korisnika i provjeri radi li se o listi. Ovisno o veličini liste, svakom
korisniku dodijeli id po redu. Potom vraća listu dictonary-a korisnika.
[{“korisnik”:“Ivan”,“id”:0},{“korisnik”:“Pero”,“id”:1}]

Druga funkcija ispisuje brojeve od 1 do 10. Ceka 0.01 sekundu poslje
svakog broja. Treća funkcija uzima listu dictonary-a korisnika i provjeri
radi li se o listi i jesu li svi elemnti dictionary. Također provjerava postoje
li ključevi korisnik i id. Čeka 0.05 sekundi. Kreira i nakraju vraća listu
tuple-a korisnika gdje dodatno svakom korisniku izraćuna duljinu imena.
[(“Ivan”,0,4), (“Pero”,1,4)]

Funkcija main prvo kreira listu imena korisnika i poziva redom funkcije, te
zavrsetkom treće funkcije zavrsava i program.
"""

import asyncio

async def func1(k):
    assert isinstance(k, list)
    return [{"korisnik": e, "id" : i} for i,e in enumerate(k)]

async def func2():
    for x in range(10):
        await asyncio.sleep(0.01)
        print(x)

async def func3(ld):
    assert isinstance(ld, list) and all([isinstance(d, dict) for d in ld])
    assert ([(d.get("korisnik") and d.get("id")) for d in ld])
    await asyncio.sleep(0.05)
    return [(d.get("korisnik"), d.get("id"), len(d.get("korisnik"))) for d in ld]

async def main():
    imena = ["Ivan", "Pero", "Ana"]
    mid_res = await func1(imena)
    asyncio.create_task(func2())
    final = await func3(mid_res)
    print(final)

if __name__ == "__main__":
    asyncio.run(main())