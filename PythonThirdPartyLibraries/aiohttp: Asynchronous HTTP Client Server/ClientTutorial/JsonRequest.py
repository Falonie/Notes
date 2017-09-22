import aiohttp, asyncio


async def page():
    async with aiohttp.ClientSession() as session:
        # async with session.post(json={'test': 'object'})
            pass