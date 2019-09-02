import functools


def decorator(f):
    @functools.wraps(f)
    def decorator_function(*args, **kwargs):
        result = f(*args, **kwargs)
        next(result)
        return result
    return decorator_function


@decorator
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming {}...'.format(n))
        r = '200 OK'


def produce(c):
    # c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing {}...'.format(n))
        r = c.send(n)
        print('[PRODUCER] Consumer return:{}'.format(r))
    c.close()

c = consumer()
# print(next(c))
# print(next(c))
# c.send(None)
# c.send(233333)

c = consumer()
produce(c)
