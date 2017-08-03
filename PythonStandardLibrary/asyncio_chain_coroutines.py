import asyncio


async def compute(x, y):
    print('Compute {} + {}...'.format(x, y))
    await asyncio.sleep(1)
    print(x + y)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print('{} + {} = {}'.format(x, y, result))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()