import asyncio

# Initialization
NODES = 10
sequences = [0] * NODES  # [0, 0, 0, 0, 0, 0, 0 ...]
buffer = {}


async def handle_connection(reader, writer):
    print("Someone is here")

    while data := await reader.readline():
        try:
            ldata = data.decode("utf8").split("-", maxsplit=2)
            sender, vector_clock, msg = int(ldata[0]), tuple(map(
                int, ldata[1].strip('[]').split(','))), ldata[2].strip()
            #print("vector_clock: ", vector_clock)

            print("Received:", sender, vector_clock, msg)
            buffer[sender, vector_clock] = msg
            # print(buffer)

            # find a message to deliver
            def deliver():
                print(f"Status: ", "-".join(map(str, sequences)))
                for (n, d), m in buffer.items():
                    # Provjeri je li za svaki node u vektorskom satu dep[i] <= Trenutnog statusa
                    if all(d[i] <= sequences[i] for i in range(NODES)):
                        # sender, dependencies, message
                        print("*** Delivering", n, d, m)
                        del buffer[n, d]
                        sequences[n] += 1
                        return True

            while deliver():
                pass

        except Exception as e:
            print(e)


async def main():
    server = await asyncio.start_server(handle_connection, "127.0.0.1", 9000)

    print(server.sockets)

    async with server:
        await server.serve_forever()

asyncio.run(main())
# __________________________________________________________________________
# Primjer rada

# Node 0 šalje poruku "Hello World!" sa deps [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#   0-[0,0,0,0,0,0,0,0,0,0]-Hello World!
# Delivering Hello World!

# Node 1 šalje poruku "Hello Again!" sa deps [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#   1-[1,0,0,0,0,0,0,0,0,0]-Hello Again!
# Delivering Hello Again!

# Node 2 šalje poruku "Goodbye!" sa deps [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
#   2-[1,2,0,0,0,0,0,0,0,0]-Goodbye!
# Sprema u buffer budući da je trenutni status: 1-1-0-0-0-0-0-0-0-0

# Node 1 šalje poruku "Hello Again!" sa deps [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#   1-[1,0,0,0,0,0,0,0,0,0]-Hello Again!
# Delivered, jer se vek sat povećava i sad je status:  1-2-0-0-0-0-0-0-0-0

# Potom dolazi i poruka "Goodbye!", te status postaje 1-2-1-0-0-0-0-0-0-0
# _________________________________________________________________________


# Terminal ispis
"""
    Someone is here
Received: 0 (0, 0, 0, 0, 0, 0, 0, 0, 0, 0) Hello World!
Status:  0-0-0-0-0-0-0-0-0-0
*** Delivering 0 (0, 0, 0, 0, 0, 0, 0, 0, 0, 0) Hello World!
Status:  1-0-0-0-0-0-0-0-0-0

Received: 1 (1, 0, 0, 0, 0, 0, 0, 0, 0, 0) Hello Again!
Status:  1-0-0-0-0-0-0-0-0-0
*** Delivering 1 (1, 0, 0, 0, 0, 0, 0, 0, 0, 0) Hello Again!
Status:  1-1-0-0-0-0-0-0-0-0

Received: 2 (1, 2, 0, 0, 0, 0, 0, 0, 0, 0) Goodbye!
Status:  1-1-0-0-0-0-0-0-0-0

Received: 1 (1, 0, 0, 0, 0, 0, 0, 0, 0, 0) Hello Again!
Status:  1-1-0-0-0-0-0-0-0-0
*** Delivering 1 (1, 0, 0, 0, 0, 0, 0, 0, 0, 0) Hello Again!
Status:  1-2-0-0-0-0-0-0-0-0

*** Delivering 2 (1, 2, 0, 0, 0, 0, 0, 0, 0, 0) Goodbye!
Status:  1-2-1-0-0-0-0-0-0-0
    """

# Broadcast requests
"""
0-[0,0,0,0,0,0,0,0,0,0]-Hello World!
1-[1,0,0,0,0,0,0,0,0,0]-Hello Again!
2-[1,2,0,0,0,0,0,0,0,0]-Goodbye!
1-[1,0,0,0,0,0,0,0,0,0]-Hello Again!
    """
