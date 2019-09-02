from redis import Redis

redis_instance = Redis(host='127.0.0.1', port=6379, password='falonie')
redis_instance.set('username', 'Falonie Wang')
# redis_instance.get('username')
print(redis_instance.get('username'))
redis_instance.delete('username')

redis_instance2 = Redis(host='127.0.0.1', port=6379, password='falonie')
# redis_instance2.lpush('languages', 'Python')
# redis_instance2.lpush('languages', 'Java')
# redis_instance2.lpush('languages', 'Go')
# redis_instance2.lpush('languages', 'C')
print(redis_instance2.lrange('languages', 0, -1))

# redis_instance.sadd('city','Tokyo')
# redis_instance.sadd('city','Beijing')
# redis_instance.sadd('city','NewYork')
# redis_instance.sadd('city','Beijing')
# redis_instance.sadd('city','Boston')
print(redis_instance.smembers('city'))

# redis_instance.hset('website','baidu','www.baidu.com')
# redis_instance.hset('website','google','www.google.com')
# redis_instance.hset('website','qq','www.qq.com')
print(redis_instance.hgetall('website'))

# pip = redis_instance.pipeline()
# pip.set('username', 'falonie')
# pip.set('password', '123456')
# pip.execute()

def sub():
    p = redis_instance.pubsub()
    p.subscribe('email')
    while True:
        for item in p.listen():
            print(item)
