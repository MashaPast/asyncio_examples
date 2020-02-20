# WS server example

import asyncio
import websockets
from logger import appLogger


async def handler(websocket, path):
    appLogger.debug('Getting message from client')
    action = await websocket.recv()

    print(f"client subscribed to action {action}")

    while True:
        await asyncio.sleep(5)
        await websocket.send("this is information")

start_server = websockets.serve(handler, "localhost", 10100)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()




