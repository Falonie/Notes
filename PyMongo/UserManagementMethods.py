import pymongo

db = pymongo.MongoClient(host='127.0.0.1', port=27017)['Falonie']
# db.add_user(name='001',password='123',role=)