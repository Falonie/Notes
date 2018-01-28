import asyncio, aiohttp, collections, tqdm
from aiohttp import web
from flags2_common import main, HTTPStatus, Result, save_flag

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


async def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = await aiohttp.request('GET', url)
    if resp.status == 200:
        image = await resp.read()
        return image
    elif resp.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.HttpProcessingError(code=resp.status, message=resp.reason, headers=resp.headers)


async def download_one(cc, base_url, semaphore, verbose):
    try:
        with (await semaphore):
            image = await get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'ok'
    if verbose and msg:
        print(cc, msg)
    return Result(status, cc)


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == '__main__':
    main(download_many)