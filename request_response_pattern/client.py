import asyncio
import websockets
from logger import appLogger


async def calculate():
    uri = "ws://localhost:8765"
    appLogger.debug('Starting connection')
    async with websockets.connect(uri) as websocket:
        letters = 'a'
        appLogger.debug('Sending message to server')
        await websocket.send(letters)
        print(letters)

        appLogger.debug('Receiving answer from server')
        result = await websocket.recv()
        print(result)

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(calculate())

