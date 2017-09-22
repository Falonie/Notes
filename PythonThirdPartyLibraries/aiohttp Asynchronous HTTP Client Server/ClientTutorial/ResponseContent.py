import aiohttp, asyncio


async def page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.text())
            # print(await response.read())
            # print(await response.json())


if __name__ == '__main__':
    url = 'https://python.org'
    # url = 'https://api.github.com/events'
    # page(url=url)
    tasks = [page(url=url)]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
