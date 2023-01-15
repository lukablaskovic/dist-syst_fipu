import asyncio


async def handler(reader, writer):  # Svaki handler mora imati reader i writer objekte
    print("Nova konekcija!")

    writer.write(b"Hello")  # Pretvara u bytove
    await writer.drain()  # Šalje, TCP congestion control

    while True:
        l = await reader.readline()
        print(l.decode("utf-8"))

# Probaj napraviti Causal broadcast


async def main():
    server = await asyncio.start_server(
        handler,  # Funkcija koja će zaprimati nove konekcije
        "127.0.0.1",
        8080
    )

    async with server:
        print("Server started!")
        await server.serve_forever()

asyncio.run(main())
