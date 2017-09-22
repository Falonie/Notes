import aiohttp, asyncio, json

url = 'https://api.github.com/some/endpoint'
url2 = 'https://api.github.com/some/endpoint'
payload = {'key1': 'value1', 'key2': 'value2'}
payload2 = {'some': 'data'}
headers = {'content-type': 'application/json'}
cookies = {'cookies_are': 'working'}


async def page():
    async with aiohttp.ClientSession() as session:
        async with session.post(url='http://httpbin.org/post', data=json.dumps(payload)) as response:
            print(await response.text())


async def page2():
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.post(url2, data=json.dumps(payload2)) as response:
            print(await response.text())


async def proxy():
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.post(url='https://python.org', ) as response:
            print(response.status)


if __name__ == '__main__':
    tasks = [page(), page2(), proxy()]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    pass