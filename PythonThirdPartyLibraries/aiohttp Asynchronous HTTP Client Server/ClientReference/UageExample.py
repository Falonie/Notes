import aiohttp, asyncio


async def fetch(client):
    async with client.get('http://python.org') as response:
        print(await response.text())


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        html = await fetch(client)
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))