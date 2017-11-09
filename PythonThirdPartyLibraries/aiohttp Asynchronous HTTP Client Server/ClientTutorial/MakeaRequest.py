import aiohttp, asyncio


async def page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            # print(response.status)
            print(await response.text())


if __name__ == '__main__':
    url1 = 'https://api.github.com/events'
    url2 = 'http://www.jianshu.com/p/cd14482184a6'
    # tasks = [page(url1)]
    tasks = [page(url1), page(url2)]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()