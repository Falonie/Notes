import functools
from collections import namedtuple

def prime_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        next(r)
        return r

    return wrapper


@prime_decorator
def my_coroutine():
    while True:
        received = yield
        print('Received', received)


# it = my_coroutine()
# it.send('falonie')
# print(it.send('falonie'))

@prime_decorator
def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


# it = minimize()
# print(it.send(10))

Query=namedtuple('Query',('y','x'))
n=Query(1,1)
print(n)