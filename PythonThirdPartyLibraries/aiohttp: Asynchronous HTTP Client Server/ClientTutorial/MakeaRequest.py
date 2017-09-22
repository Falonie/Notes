import aiohttp, asyncio


async def page():
    async with aiohttp.ClientSession() as session:
        async with session.get(url='https://api.github.com/events') as response:
            print(response.status)
            print(await response.text())


if __name__ == '__main__':
    tasks = [page()]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
