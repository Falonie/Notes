import requests, re, pymongo, time, xlrd
from lxml import html
from multiprocessing import Pool

url = 'http://www.newseed.cn/project/61926'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
cookies = {
    'Cookie': 'ARRAffinity=197ae5372184c64aeca47f780a2e053f3a50366e2bda392cd4bfa3b38e39a929; __uid=7708072285; __utmt=1; ASP.NET_SessionId=l3ey4acdym3sk2mjtjmxn5rd; pedaily.cn=uid=201531&username=18516630543&password=9724D8CA473B50D9B007DAE52181AFD7&email=&mobile=18516630543&oauth_token=&oauth_token_secret=&unionid=&hiname=%E6%96%B0%E8%8A%BD%E7%BD%91%E5%8F%8B721531&photo=&blogurl=&usertype=0&companyid=0&logintype=12&roletype=0&ismobilevalidated=True&isemailvalidated=False&isverified=False&isok=False; jiathis_rdc=%7B%22http%3A//www.newseed.cn/project/62156%22%3A%220%7C1513836386928%22%7D; __utma=117171865.1601227618.1513836341.1513836341.1513836341.1; __utmb=117171865.5.10.1513836341; __utmc=117171865; __utmz=117171865.1513836341.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); zg_did=%7B%22did%22%3A%20%2216077ad63fc158-017288883860d9-464a0129-e1000-16077ad63fd5b%22%7D; zg_2804ec8ba91741c0853e364274858816=%7B%22sid%22%3A%201513836340227%2C%22updated%22%3A%201513836391712%2C%22info%22%3A%201513836340233%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22201531%22%7D; Hm_lvt_155833ecab8e70af6f2498f897bd8616=1513836341; Hm_lpvt_155833ecab8e70af6f2498f897bd8616=1513836392; Hm_lvt_25919c38fb62b67cfb40d17ce3348508=1513836341; Hm_lpvt_25919c38fb62b67cfb40d17ce3348508=1513836392'}
db = pymongo.MongoClient(host='localhost', port=27017)['Falonie']
collection_crawled = db['newseed_Pre-A_crawled_result']
collection=db['newseed_Pre-A_urls']
test_urls = ['http://www.newseed.cn/project/35361', 'http://www.newseed.cn/project/35154',
             'http://www.newseed.cn/project/34386', 'http://www.newseed.cn/project/33610',
             'http://www.newseed.cn/project/30502']
file = 'newseed_种子_urls.xlsx'


def read_excel(file):
    with xlrd.open_workbook(file) as data_:
        table = data_.sheets()[0]
        # for rownum in range(0, table.nrows):
        #     row = table.row_values(rownum)
        #     yield row[0]
        # urls_list = [table.row_values(rownum)[0] for rownum in range(0, table.nrows)]
        urls_list = [table.row_values(rownum)[0] for rownum in range(100, table.nrows)]
        return urls_list


def read_mongodb():
    collection = db['newseed_Pre-A_urls']
    urls = [_['url'] for _ in collection.find({})]
    return urls

def uncrawled_urls():
    urls = [_['url'] for _ in list(collection.find({}))]
    urls_crawled = [_['url'] for _ in list(collection_crawled.find({}))]
    uncrawled_urls_=list(set(urls)-set(urls_crawled))#.__len__()
    return uncrawled_urls_

def parse_url(url):
    session = requests.session()
    r = session.get(url=url, headers=header, cookies=cookies).text
    selector = html.fromstring(r)
    for _ in selector.xpath('//div[@class="info-box"]/div[@class="info"]'):
        product = _.xpath('h1/text()')
        product = ''.join(str(i).strip() for i in product)
        field = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[1]/a/text()')
        field = ''.join(str(i).strip() for i in field)
        platform = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[2]/span[1]/text()')
        platform = ''.join(str(i).strip() for i in platform)
        location = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[2]/span[2]/text()')
        location = ''.join(str(i).strip() for i in location)
        homepage = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[3]/span[1]/descendant::text()')
        homepage = ''.join(str(i).strip() for i in homepage)
        establish_time = _.xpath('ul[@class="subinfo"]/li[@class="r box-fix-r"]/p[1]/text()')
        establish_time = ''.join(str(i).strip() for i in establish_time)
        status = _.xpath('ul[@class="subinfo"]/li[@class="r box-fix-r"]/p[2]/text()')
        status = ''.join(str(i).strip() for i in status)
        tags = selector.xpath('//div[@class="project-top"]/div[@class="txt"]/div[1]/a/text()')
        tags = ''.join(str(i).strip() for i in tags)
        description = selector.xpath('//div[@class="box-plate"]/div[@class="desc"]/text()')
        description = re.sub(r'[\n\r ]', '', ''.join(str(i).strip() for i in description))
        contact = _.xpath('//div[@class="project-status"]/div[@class="people-list"]/h4[@class="title"]/a/text()')
        contact = ''.join(str(i).strip() for i in contact)
        leadership = selector.xpath('//div[@class="item-list people-list"]/ul/li/div[2]/descendant::text()')
        leadership = list(filter(lambda x: len(x) > 1, [str(_).strip() for _ in leadership]))
        logo_url = selector.xpath('//div[@class="img"]/span[@class="img-middle"]/img/@src')
        logo_url = ''.join(str(i).strip() for i in logo_url)
        # print(product,field,platform,location,homepage,establish_time,status,tags,description)
        item = {'product': product, 'field': field, 'platform': platform, 'location': location, 'homepage': homepage,
                'establish_time': establish_time, 'status': status, 'tags': tags, 'description': description,
                'contact': contact, 'leadership': leadership, 'logo_url': logo_url, 'url': url}
        collection.insert(item)
        return item


def manage_read_excel():
    t0 = time.time()
    for i, j in enumerate(read_excel(file), 1):
        print(i, parse_url(j))
    print(time.time() - t0)


def manage():
    t0 = time.time()
    with Pool() as pool:
        # p = pool.map(parse_url, read_excel(file))
        # p = pool.map(parse_url, read_mongodb())
        p = pool.map(parse_url, uncrawled_urls())
        for i, j in enumerate(p, 1):
            print(i, j)
            try:
                collection_crawled.insert(j)
            except Exception as e:
                print(e)
    print(time.time() - t0)


if __name__ == '__main__':
    # print(read_mongodb().__len__())
    # print(parse_url('http://www.newseed.cn/project/30502'))
    manage()
    # print(uncrawled_urls().__len__())
    # manage_read_excel()
    # print(read_excel(file))