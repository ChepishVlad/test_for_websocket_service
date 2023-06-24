import asyncio
import json
import sys

import websockets


async def do_smth():
    uri = "ws://127.0.0.1:4000"
    async with websockets.connect(uri) as ws:
        await ws.send('{"method": "add", "id": "sfda-11231-123-adfa", "name": "name", "surname":"surname", "phone":"123123123", "age": 12}')
        repl = await ws.recv()
        print (json.loads(repl))

        await ws.send('{"method": "select", "id": "sfda-11231-123-adss", "phone": "123123123"}')
        repl_s = await ws.recv()
        print(repl_s)

        await ws.send(
            '{"method": "add", "id": "sfda-11231-123-adfa", "name": "name", "surname":"surname", "phone":"123123123", "age": 12}')
        repl = await ws.recv()
        print(json.loads(repl))


if __name__ == '__main__':
# asyncio.get_event_loop().run_until_complete(do_smth())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_smth())
    loop.close()