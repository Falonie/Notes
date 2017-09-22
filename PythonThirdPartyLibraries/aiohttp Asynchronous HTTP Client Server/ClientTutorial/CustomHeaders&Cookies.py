import aiohttp, asyncio, json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
url2='http://httpbin.org/cookies'
cookies={'cookies_are':'working'}

async def page():
    async with aiohttp.ClientSession() as session:
        await session.post(url=url, data=json.dumps(payload), headers=headers)

async def page2():
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.get(url2) as response:
            print(await response.json())

if __name__ == '__main__':
    tasks = [page2()]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    pass