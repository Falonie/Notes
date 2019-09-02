from lxml import etree
from time import time
import asyncio
import aiohttp

url = 'https://movie.douban.com/top250'


async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def parse(url):
    page = await fetch_content(url)
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = [url + p.get('href') for p in pages]
    result = [element_movie for element_movie in html.xpath(xpath_movie)]

    # for element_movie in html.xpath(xpath_movie):
    #     result.append(element_movie)

    # for p in pages:
    #     fetch_list.append(url + p.get('href'))

    tasks = [fetch_content(url) for url in fetch_list]
    pages_details = await asyncio.gather(*tasks)

    # for page in pages_details:
    #     html = etree.HTML(page)
    #     for element_movie in html.xpath(xpath_movie):
    #         result.append(element_movie)
    #
    # for i, movie in enumerate(result, 1):
    #     title = movie.find(xpath_title).text
    #     print(i, title)
    #
    # for p in pages_details:
    #     selector = etree.HTML(p)
    #     for i,_ in enumerate(selector.xpath('//div[@class="info"]/div[1]/a/span[1]/text()')):
    #         print(i,_)

    for page in pages_details:
        html = etree.HTML(page)
        for element_movie in html.xpath('//div[@class="info"]/div[1]/a/span[1]/text()'):
            print(element_movie)



def main():
    loop = asyncio.get_event_loop()
    start = time()
    # for i in range(5):
    loop.run_until_complete(parse(url))
    end = time()
    print('Cost {} seconds'.format((end - start)))
    loop.close()


if __name__ == '__main__':
    main()
