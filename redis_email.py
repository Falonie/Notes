from redis import Redis

redis_instance = Redis(host='127.0.0.1', port=6379, password='falonie')
for _ in range(3):
    redis_instance.publish('email', '541002901@qq.com')
