import asyncio
import websockets


async def calculate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        letters = 'a'

        await websocket.send(letters)
        print(letters)

        result = await websocket.recv()
        print(result)

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(calculate())

