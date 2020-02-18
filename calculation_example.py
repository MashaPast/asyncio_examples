import asyncio
import time


async def get_num1():
    await asyncio.sleep(1)
    num1 = 2 * 2
    return num1


async def get_num2():
    await asyncio.sleep(1)
    num2 = 3 * 2
    return num2


async def main():
    start = time.time()
    result = await asyncio.gather(get_num1(), get_num2())
    answer = 1
    for el in result:
        answer *= el
    print(answer)
    finish = time.time()
    print(finish - start)


ioloop = asyncio.get_event_loop()
tasks = [main()]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()