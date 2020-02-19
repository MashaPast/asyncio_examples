# WS server example

import asyncio
import websockets
from client_server_hello.logger import appLogger



async def hello(websocket, path):
    appLogger.debug('Getting message from client')
    name = await websocket.recv()

    print(f"< {name}")

    greeting = f"Hello {name}!"

    appLogger.debug('Sending message to client')
    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# On the server side, websockets executes the handler coroutine hello once for each WebSocket connection. It closes the connection when the handler coroutine returns.


