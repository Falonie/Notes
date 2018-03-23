import pymongo
import os

db = pymongo.MongoClient(host='127.0.0.1', port=27017)['Falonie']
collection = db['maigoo_车 / 建工 / 农具']
collection2 = db['maigoo_家饰家纺房产']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)

# collection.rename('maigou')
print(os.getcwd())
# collection.drop()