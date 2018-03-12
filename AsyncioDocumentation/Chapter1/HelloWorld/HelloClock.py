import asyncio


async def print_every_second():
    while True:
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)


async def print_every_minute():
    for i in range(10):
        await asyncio.sleep(60)
        print(i, 'minute')


loop = asyncio.get_event_loop()
# tasks=
loop.run_until_complete(asyncio.gather(print_every_minute(), print_every_second()))
loop.close()
