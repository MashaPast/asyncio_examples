import websockets
import asyncio

async def calculate(websocket, path):
    str_recieved = await websocket.recv()
    print(str_recieved)

    result = str_recieved + 'b'
    await websocket.send(result)
    print(result)

start_server = websockets.serve(calculate, "localhost", 8765)

ioloop = asyncio.get_event_loop()

ioloop.run_until_complete(start_server)
ioloop.run_forever()

