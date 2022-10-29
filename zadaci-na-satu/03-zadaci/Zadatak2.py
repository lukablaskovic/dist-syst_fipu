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