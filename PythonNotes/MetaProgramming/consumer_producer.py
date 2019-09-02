import functools


def decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func = f(*args, **kwargs)
        # next(func)
        func.send(None)
        return func
    return wrapper


@decorator
def consumer():
    while True:
        received = yield
        print('Received: ', received)


def producer(c):
    for _ in range(10):
        c.send(_)


c = consumer()
# c.send(None)
c.send(2)
c.send('falonie')

# producer(consumer())
