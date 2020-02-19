# WS client example
import asyncio
import websockets
import time
from client_server_hello.logger import appLogger


async def hello():
    uri = "ws://localhost:8765"
    appLogger.debug('Start connection')
    async with websockets.connect(uri) as websocket:
        name = 'r'

        appLogger.debug('Sending message to server')

        await websocket.send(name)
        print(f"> {name}")

        appLogger.debug('Getting message from server')

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())


