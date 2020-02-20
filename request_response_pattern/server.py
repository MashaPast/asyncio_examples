import websockets
import asyncio
from logger import appLogger


async def calculate(websocket, path):
    appLogger.debug('Receiving message from server')
    str_recieved = await websocket.recv()
    print(str_recieved)

    appLogger.debug('Processing data')
    result = str_recieved + 'b'

    appLogger.debug('Sending answer to client')
    await websocket.send(result)
    print(result)

start_server = websockets.serve(calculate, "localhost", 8765)

ioloop = asyncio.get_event_loop()

ioloop.run_until_complete(start_server)
ioloop.run_forever()

