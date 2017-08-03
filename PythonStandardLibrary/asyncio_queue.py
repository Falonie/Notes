import asyncio, random


async def produce(queue, n):
    for x in range(n):
        print('producing {}/{}'.format(x, n))
        await asyncio.sleep(1)
        item = str(x)
        await queue.put(item)


async def consume(queue):
    while True:
        item = await queue.get()
        print('consuming {}...'.format(item))
        await asyncio.sleep(random.random())
        queue.task_done()


async def run(n):
    queue = asyncio.Queue()
    consumer = asyncio.ensure_future(consume(queue=queue))
    await produce(queue=queue, n=n)
    await queue.join()
    consumer.cancel()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(10))
    loop.close()