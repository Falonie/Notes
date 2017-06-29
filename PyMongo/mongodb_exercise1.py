import pymongo,datetime

client=pymongo.MongoClient()
db=client.py_database
#collection=db.py_collection

post={'author':'Mike',
      'text':'My first blog post!',
      'tags':['mongodb','python','pymongo'],
      'date':datetime.datetime.utcnow()}
test1=db.test1
#test1.insert_one(post)
print(test1.find_one())
print(test1.find_one({'author':"Mike"}))

new_post=[{'author':"Mike",
          'text':"anothor post",
          'tags':['bulk0,''inset'],
          'date':datetime.datetime.utcnow()},
          {'author':"Elit",
          'text':"Mongodb",
          'tags':['bulk0,''inset'],
          'date':datetime.datetime.utcnow()}]
#result=test1.insert_many(new_post)
for i in test1.find():
    print(i)
print('\n')

for i in test1.find({'author':'Mike'}):
    print(i)
print(test1.find({'author':'Mike'}).count())
print('\n')

test2=db.test2
data=[{'x':1},{'x':1},{'x':1}]
#test2.insert_many(data)
for i in test2.find():
    print(i)

#test2.update_one({"x":1},{'$set':{'x':3}},upsert=True)
for i in test2.find():
    print(i)
print('\n')

#test2.update_one({'x':4},{'$set':{"x":23333}},upsert=True)
for i in test2.find():
    print(i)
print('\n')

# test2.update_many({'x':1},{'$set':{'x':'manager'}},upsert=True)
for i in test2.find():
    print(i)
print('\n')

#test2.update_many({'x':3},{'$set':{'x':1,"y":2}},upsert=True)
#test2.update()
for i in test2.find():
    print(i)

#test2.remove({'x':23333})

#print(test2.getIndexes())

test3=db.test3
#test3.insert({'x':1})
# test3.getIndexes()
print(test3.find_one())