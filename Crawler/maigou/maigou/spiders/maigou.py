import scrapy, re
from ..items import MaigouItem


class MaigouSpider(scrapy.Spider):
    name = 'maigou'
    # 车 / 建工 / 农具
    start_url7=[
        # 'http://10.maigoo.com/search/?catid=9&areaid=3258&action=ajax&getac=brand&page={page}',
        # 'http://10.maigoo.com/search/?catid=9&areaid=3288&action=ajax&getac=brand&page={page}',
        # 'http://10.maigoo.com/search/?catid=9&areaid=2754&action=ajax&getac=brand&page={page}',
        # 'http://10.maigoo.com/search/?catid=9&areaid=3076&action=ajax&getac=brand&page={page}',
        # 'http://10.maigoo.com/search/?catid=9&areaid=3162&action=ajax&getac=brand&page={page}',
        'http://10.maigoo.com/search/?catid=9&areaid=3142&action=ajax&getac=brand&page={page}',
        'http://10.maigoo.com/search/?catid=9&areaid=3153&action=ajax&getac=brand&page={page}'
    ]

    # def start_requests(self):
    #     for i in range(5, 250):
    #         url = self.start_urls[0].format(page=i)
    #         yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def start_requests(self):
        for start_url in self.start_url7:
            for i in range(80, 100):
                url = start_url.format(page=i)
                yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        # print(response)
        # print(type(response), type(response.body), type(response.body.decode('utf-8')))
        r = response.body.decode('utf-8')
        r1 = response.body
        pattern = re.compile(r'<a class="dhidden" href="(.*?)" target="_blank">')
        # for i in pattern.findall(str(r1)):
        for href in pattern.findall(r):
            item = {'href': href}
            yield scrapy.Request(url=href, meta={'item': item}, dont_filter=True, callback=self.page_details)

    def page_details(self, response):
        selector = scrapy.Selector(response)
        maigou = response.meta.get('item', '')
        name = selector.xpath('//ul[@class="info fr"]/li[@class="name"]/text()|'
                              '//ul[@class="info long"]/li[@class="name"]/text()|'
                              '//div[@class="b_company_info"]/div[@class="b-ttl"]/text()').extract_first(default='N/A')
        maigou['company'] = re.sub(r'[\n ]','',''.join(str(i).strip() for i in name))
        for item in selector.xpath('//ul[@class="info col3 noweixin"]/li[position()<6]'):
            n = item.xpath('text()|b/font/text()|a/text()').extract()
            try:
                a, b = ''.join(str(i).strip().replace('\n', '') for i in n).split('：')
            except Exception as e:
                a = ''.join(str(i).strip().replace('\n', '') for i in n).split('：')[0]
                b = 'N/A'
            finally:
                maigou[a] = b
        for item in selector.xpath('//ul[@class="info fr"]/li[position()>1]'):
            a, b = ''.join(str(i).strip() for i in item.xpath('text()|a/text()').extract()).split('：')
            # name = selector.xpath('//ul[@class="info fr"]/li[@class="name"]/text()').extract_first('N/A')
            # print(a, b)
            maigou[a] = b
            # maigou['company'] = name
        for item in selector.xpath('//ul[@class="license"]/li'):
            try:
                a, b = ''.join(str(i).strip() for i in item.xpath('text()|a/text()').extract()).split('：')
            except Exception as e:
                a, b = ''.join(str(i).strip() for i in item.xpath('text()|a/text()').extract()).split('：')[0], 'N/A'
            finally:
                maigou[a] = b
        brief = selector.xpath('//div[@class="introduce"]/div[@class="desc"]/p/text()').extract()
        maigou['brief'] = re.sub(r'[\n\r\xa0 ]', '', ''.join(str(i) for i in brief))
        yield maigou