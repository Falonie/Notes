import requests, re, pymongo, time
from lxml import html
from multiprocessing import Pool

url = 'http://www.newseed.cn/project/p2'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
cookies = {
    'Cookie': 'ARRAffinity=197ae5372184c64aeca47f780a2e053f3a50366e2bda392cd4bfa3b38e39a929; __uid=7708072285; __utmt=1; ASP.NET_SessionId=l3ey4acdym3sk2mjtjmxn5rd; pedaily.cn=uid=201531&username=18516630543&password=9724D8CA473B50D9B007DAE52181AFD7&email=&mobile=18516630543&oauth_token=&oauth_token_secret=&unionid=&hiname=%E6%96%B0%E8%8A%BD%E7%BD%91%E5%8F%8B721531&photo=&blogurl=&usertype=0&companyid=0&logintype=12&roletype=0&ismobilevalidated=True&isemailvalidated=False&isverified=False&isok=False; jiathis_rdc=%7B%22http%3A//www.newseed.cn/project/62156%22%3A%220%7C1513836386928%22%7D; __utma=117171865.1601227618.1513836341.1513836341.1513836341.1; __utmb=117171865.5.10.1513836341; __utmc=117171865; __utmz=117171865.1513836341.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); zg_did=%7B%22did%22%3A%20%2216077ad63fc158-017288883860d9-464a0129-e1000-16077ad63fd5b%22%7D; zg_2804ec8ba91741c0853e364274858816=%7B%22sid%22%3A%201513836340227%2C%22updated%22%3A%201513836391712%2C%22info%22%3A%201513836340233%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22201531%22%7D; Hm_lvt_155833ecab8e70af6f2498f897bd8616=1513836341; Hm_lpvt_155833ecab8e70af6f2498f897bd8616=1513836392; Hm_lvt_25919c38fb62b67cfb40d17ce3348508=1513836341; Hm_lpvt_25919c38fb62b67cfb40d17ce3348508=1513836392'}
collection = pymongo.MongoClient(host='localhost', port=27017)['Falonie']['newseed_Pre-A_urls']
page_urls = ['http://www.newseed.cn/project/r17-p{}'.format(_) for _ in range(1, 107)]
# print(page_urls)


def get_urls(url):
    session = requests.session()
    r = session.get(url=url, headers=header, cookies=cookies).text
    selector = html.fromstring(r)
    urls = []
    for _ in selector.xpath('//div[@class="project-list"]/table[@class="table-list"]/tbody/tr[position()>1]'):
        href = _.xpath('td[1]/a/@href')
        href = ''.join(str(i) for i in href)
        urls.append(href)
    urls_dict = [{'url': _} for _ in urls]
    return urls_dict


def manage():
    t0 = time.time()
    with Pool() as pool:
        p = pool.map(get_urls, page_urls)
        for i, j in enumerate(p, 1):
            print(i, j)
            try:
                collection.insert_many(j)
            except Exception as e:
                print(e)
    print(time.time() - t0)


if __name__ == '__main__':
    manage()
    # print(get_urls('http://www.newseed.cn/project/r15-p79'))
    # print(page_urls)