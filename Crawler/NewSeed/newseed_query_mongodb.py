import pymongo,os

collection_crawled = pymongo.MongoClient(host='localhost', port=27017)['Falonie']['newseed_Pre-A_crawled_result']
collection=pymongo.MongoClient(host='localhost', port=27017)['Falonie']['newseed_Pre-A_urls']
for i, j in enumerate(collection_crawled.find({}), 1):
    # print(i, j)
    pass

urls=[_['url'] for _ in list(collection.find({}))]
print(urls.__len__())
print(set(urls).__len__())
urls_crawled=[_['url'] for _ in list(collection_crawled.find({}))]
print(urls_crawled.__len__())
urls_uncrawled=[]
for _ in urls:
    if _ not in urls_crawled:
        urls_uncrawled.append(_)
print(urls_uncrawled.__len__())
print(set(urls_uncrawled).__len__())
print(list(set(urls)-set(urls_crawled)).__len__())
# print(set(urls)-set(urls_crawled))
# collection.drop()
print(os.path.abspath('.'))