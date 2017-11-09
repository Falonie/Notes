import aiohttp, asyncio


async def page(url):
    response = await aiohttp.request(method='GET', url=url)
    print(url, response)
    response.close()
    # with await aiohttp.request(method='GET', url=url) as response:
    #     print(url, response)


async def page2(url):
    async with aiohttp.ClientSession() as session:
        # print('Finished.', url)
        async with session.get(url=url) as html:
            text = await html.text()
            print(text)


if __name__ == '__main__':
    tasks = [page('http://www.jianshu.com/p/cd14482184a6'), page('https://github.com/awolfly9?tab=repositories')]
    # tasks = [page2('http://www.jianshu.com/p/cd14482184a6'), page2('https://github.com/awolfly9?tab=repositories')]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()