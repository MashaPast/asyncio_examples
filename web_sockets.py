import asyncio
import websockets
import datetime
import time

uri = "wss://api-pub.bitfinex.com/ws/2"


async def recieve(data_to_send):
    async with websockets.connect(uri) as websocket:

        await websocket.send(data_to_send)
        print(f"> {data_to_send}")

        response_data = await websocket.recv()
        print(f"< {response_data}")


async def main():
    print(datetime.datetime.now().strftime("%A, %B %d, %I:%M %p"))
    print('---------------------------')

    await asyncio.gather(
        recieve('{ "event": "subscribe", "channel": "ticker", "symbol": "tBTCUSD"}'),
        recieve('{ "event": "subscribe", "channel": "ticker", "symbol": "tLTCUSD"}'),
    )

start = time.time()
ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(main())]
ioloop.run_until_complete(asyncio.wait(tasks))
finish = time.time()
print("Execution time is {}".format(finish-start))
ioloop.close()

