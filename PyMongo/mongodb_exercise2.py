from pymongo import MongoClient,ASCENDING
import datetime,pprint,pymongo
from bson.objectid import ObjectId

client=MongoClient()
db=client['test_database']
collection=db['test-collection']

post={'author':'Mike',
      'text':'My first blog post!',
      'tags':['mongodb','python','pymongo'],
      'date':datetime.datetime.utcnow()}
posts=db.posts
# post_id=posts.insert_one(post).inserted_id
# post_id

print(db.collection_names(include_system_collections=False))

pprint.pprint(posts.find_one())
print(posts.find_one(),'\n')

pprint.pprint(posts.find_one({'author':'Mike'}))

print('\n','Querying By ObjectId')
# pprint.pprint(posts.find_one({'_id':post_id}))

#Bulk Inserts
print('\n','Bulk Inserts')
new_posts=[{'author':'Mike','text':'Another post!','tags':['bulk','insert'],'date':datetime.datetime(2009,11,12,11,14)},
           {'author':'Eliot','title':'MongoDB is fun','text':'and pretty easy too!','date':datetime.datetime(2009,11,10,10,45)}]
# result=posts.insert_many(new_posts)
# print(result.inserted_ids)

#Querying for More Than One Document
print('\n','Querying for More Than One Document')
for post in posts.find():
    pprint.pprint(post)

print('\n')
for post in posts.find({'author':'Mike'}):
    pprint.pprint(post)

#Counting
print('\n','Counting')
print(posts.count())
print(db.posts.find().count())
print(db.collection_names())
print(db.posts.find_one({'author':'Mike'}))

#Indexing
print('\n','Indexing')
result=db.profiles.create_index([('user_id',ASCENDING)],unique=True)
print(sorted(list(db.profiles.index_information())))

#db.posts.remove()