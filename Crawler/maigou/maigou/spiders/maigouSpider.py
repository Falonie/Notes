import requests
import re
import time
import xlrd
import json
import pymongo
from lxml import html

BASE_URL='http://10.maigoo.com/search/?catid=9&areaid=3142&action=ajax&getac=brand&page={}'

class MaigouSpider(object):
    def generate_url(self):
        page_num = 53
        # while page_num < 7:
        while True:
            url = BASE_URL.format(page_num)
            yield url
            page_num += 1

    def parse(self, url):
        # r = response.body.decode('utf-8')
        r = requests.get(url).text
        # r1 = response.body
        pattern = re.compile(r'<a class="dhidden" href="(.*?)" target="_blank">')
        print(r)
        # for href in pattern.findall(r):
        #     item = {'href': href}
        #     print(item)

if __name__ == '__main__':
    maigou=MaigouSpider()
    maigou.parse(BASE_URL.format(1))