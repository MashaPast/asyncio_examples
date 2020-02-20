# WS client example
import asyncio
import websockets
from logger import appLogger

uri = "ws://localhost:10100"


async def start_client():
    appLogger.debug('Start connection')
    ws_connection = await websockets.connect(uri)
    return ws_connection


async def subscribe_to_action(ws_connection):
    appLogger.debug('Subscribing to server')
    await ws_connection.send('blabla')
    async for message in ws_connection: #permanently
        print(message)


ws = asyncio.get_event_loop().run_until_complete(start_client())
asyncio.get_event_loop().run_until_complete(subscribe_to_action(ws))



