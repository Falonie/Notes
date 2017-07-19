import pymongo,time,logging

class MongoDB(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client['employee']
        self.collection = self.db['MongoDB_writespeed_comparision']
        self.fomatter = '%(filename)s %(funcName)s %(asctime)s %(name)s %(message)s'
        self.filename = 'insert&insert_many_writespeed_comparsions'

class MongoDB_insertone(MongoDB):
    def __init__(self):
        super().__init__()

    def process_insertone(self):
        # fomatter = '%(filename)s %(funcname)s %(asctime)s %(name)s %(message)s'
        # logging.basicConfig(filename='insert&insert_many_writespeed_comparsions',format=fomatter,level=logging.DEBUG)
        logging.basicConfig(filename=self.filename, format=self.fomatter, level=logging.DEBUG)
        t0 = time.time()
        for i in range(50000):
            self.collection.insert({'InsertOne': i})
        t = time.time() - t0
        logging.debug(t)
        # print(t)

    def select(self):
        for i in self.collection.find({}):
            print(i)

class MongoDB_insertmany(MongoDB):
    def __init__(self):
        super().__init__()

    def process_insertmany(self):
        # fomatter = '%(filename)s %(asctime)s %(name)s %(message)s'
        logging.basicConfig(filename=self.filename, format=self.fomatter, level=logging.DEBUG)
        t0 = time.time()
        insert_many = []
        for i in range(50000, 100000):
            num = {'InsertMany': i}
            insert_many.append(num)
        self.collection.insert_many(insert_many)
        t = time.time() - t0
        logging.debug(t)

    def select(self):
        for i in self.collection.find({}):
            print(i)

if __name__ == '__main__':
    mongo = MongoDB_insertone()
    # mongo.process_insertone()
    # mongo.collection.drop()
    # mongo.select()
    mongodb_insertmany = MongoDB_insertmany()
    # mongodb_insertmany.process_insertmany()
    # mongodb_insertmany.collection.drop()
    mongodb_insertmany.select()