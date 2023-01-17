import asyncio
import argparse
# Initialization
NODES = 10
sequences = [0] * NODES  # [0, 0, 0, 0, 0, 0, 0 ...]
buffer = {}


async def handle_connection(reader, writer):
    print("Someone is here")

    while data := await reader.readline():
        try:
            ldata = data.decode("utf8").split(",", maxsplit=2)
            sender, seq, msg = int(ldata[0]), int(ldata[1]), ldata[2].strip()

            print("Received:", sender, seq, msg)
            buffer[sender, seq] = msg
            # print(buffer)
            # find a message to deliver

            def deliver():
                print(f"Status: ", "-".join(map(str, sequences)))
                for n, x in enumerate(sequences):
                    if (n, x) in buffer:
                        # sender, delivered[sender], message
                        print("*** Delivering", n, x, buffer[n, x])
                        del buffer[n, x]
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

#0,0, Hello
# Node 0, šaljem nultu poruku
