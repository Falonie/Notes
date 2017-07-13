from functools import wraps

def deco(func):
    @wraps(func)
    def inner(*args,**kwargs):
        return 'running inner() {} {}'.format(func.__name__, func(*args, **kwargs))
    return inner
@deco
def target():
    return 'running target()'

if __name__ == '__main__':
    print(target())