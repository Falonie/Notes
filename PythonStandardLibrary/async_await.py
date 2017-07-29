import asyncio, time


async def hello():
    print('Hello world')
    r = await asyncio.sleep(1)
    # time.sleep(1)
    print('Hello again!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()