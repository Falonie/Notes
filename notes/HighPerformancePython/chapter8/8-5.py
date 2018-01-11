import asyncio, aiohttp, random, string


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))


def chunked_http_client(num_chunks):
    semaphore = asyncio.Semaphore(num_chunks)

    async def http_get(url):
        nonlocal semaphore
        with (await semaphore):
            response = await aiohttp.request('GET', url)
            body = await response.content.read()
            await response.wait_for_close()
        return body

    return http_get


def run_experiment(base_url, num_iter=50):
    urls = generate_urls(base_url, num_iter)
    http_client = chunked_http_client(100)
    tasks = [chunked_http_client(url) for url in urls]
    response_sum = 0
    for future in asyncio.as_completed(tasks):
        data = future
        response_sum += len(data)
    return response_sum


if __name__ == '__main__':
    import time

    delay = 100
    num_iter = 500
    base_url = 'http://127.0.0.1:8080/add?name=asyncio&delay={}'.format(delay)
    loop = asyncio.get_event_loop()
    start = time.time()
    result = loop.run_until_complete(run_experiment(base_url, num_iter))
    end = time.time()
    print("{] {}".format(result, end - result))