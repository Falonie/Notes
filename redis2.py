from redis import Redis

connection = Redis(host='127.0.0.1', port=6379, password='falonie')
print(connection.get('telephone'))

# 1 sting

# print(connection.keys('*'))
# print(connection.set('secret', 'ni!'))
# print(connection.set('carats', 24))
# print(connection.set('fever', '101.5'))

# print(connection.get('secret'))
# print(connection.get('carats'))
# print(connection.get('fever'))

# print(connection.setnx('secret', 'yewjewdsjkew'))
# print(connection.get('secret'))
# print(connection.getset('secret', 'yewjewdsjkew'))
# print(connection.get('secret').decode('utf8'))

# print(connection.getrange('secret', -6, -1))
# print(connection.setrange('secret', 0, '888'))
# print(connection.get('secret'))

# print(connection.mset({'pie': 'cherry', 'cordial': 'sherry'}))
# print(connection.mget(['pie', 'cordial', 'fever']))
# print(connection.delete('fever'))

# print(connection.get('carats'))
# print(connection.incr('carats'))
# print(connection.get('carats'))
# print(connection.incr('carats', 10))
# print(connection.decr('carats'))
# print(connection.decr('carats', 15))

# print(connection.set('fever', '101.5'))
# print(connection.incrbyfloat('fever'))
# print(connection.incrbyfloat('fever', 0.5))
# print(connection.incrbyfloat('fever', -2))

# 2 list
# print(connection.lpush('zoo', 'bear'))
# print(connection.lpush('zoo', 'alligator', 'bear'))
# print(connection.linsert('zoo', 'before', 'bear', 'beaver'))
# print(connection.linsert('zoo', 'after', 'bear', 'cassowary'))
# print(connection.lset('zoo', 2, 'marmoset'))
# print(connection.rpush('zoo', 'yak'))
# print(connection.lindex('zoo', 3))
# print(connection.lrange('zoo', 0, -1))
# print(connection.ltrim('zoo', 1, 4))
# print(connection.lrange('zoo', 0, -1))

# 3 hashtable
# print(connection.hmset('song', {'do': 'a deer', 're': 'about a deer'}))
# print(connection.hgetall('song'))
# print(connection.hset('song', 'mi', 'a note to follow me'))
# print(connection.hget('song', 'mi'))
# print(connection.hmget('song', 'do', 're'))
# print(connection.hkeys('song'))
# print(connection.hvals('song'))
# print(connection.hlen('song'))
# print(connection.hgetall('song'))

# 4 set
# print()
# connection.sadd('zooo', 'duck')
# connection.sadd('zooo', 'goat', 'turkey')
# connection.sadd('city', 'Aukland')
# print(connection.scard('zooo'))
# print(connection.smembers('zooo'))
# print(connection.srem('zooo', 'turkey'))
# print(connection.sadd('better_zoo', 'tiger', 'wolf', 'duck'))
# print(connection.sinter('zooo', 'better_zoo'))
# print(connection.sinterstore('fowl', 'zooo', 'better_zoo'))
# print(connection.smembers('fowl'))
# print(connection.sunion('zooo', 'better_zoo'))
# print(connection.sunionstore('fabulous', 'zooo', 'better_zoo'))
# print(connection.smembers('fabulous'))
# print(connection.sdiff('zooo', 'better_zoo'))
# print(connection.sdiffstore('zoo_sale', 'zooo', 'better_zoo'))
# print(connection.smembers('zoo_sale'))

# 5 sorted set
