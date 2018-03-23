import pymongo,os
collection_crawled = pymongo.MongoClient(host='localhost', port=27017)['Falonie']['newseed_天使_crawled_result']
for i, j in enumerate(collection_crawled.find({}), 1):
    print(i, j)
    pass
# collection_crawled.drop()