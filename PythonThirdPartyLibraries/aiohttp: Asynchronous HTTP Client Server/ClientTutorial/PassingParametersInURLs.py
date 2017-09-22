import aiohttp, asyncio

params = {'key1': 'value1', 'key2': 'value2'}
params2 = [('key1', 'value1'), ('key2', 'value2')]


async def page():
    async with aiohttp.ClientSession() as session:
        async with session.get(url='http://httpbin.org/get', params=params) as response:
            print(response.url)
            # assert str(response.url)=='http://httpbin.org/get?key1=value1&key2=value2'
        async with session.get(url='http://httpbin.org/get', params=params2) as r:
            print(r.url)


async def page2():
    async with aiohttp.ClientSession() as session:
        async with session.get(url='http://httpbin.org/get', params='key=value1') as r2:
            print(r2.url, type(r2.url), type(str(r2.url)))


if __name__ == '__main__':
    tasks = [page(), page2()]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
