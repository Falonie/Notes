from functools import wraps

def deco(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # print(result)
        # print('running inner() {}'.format(func.__name__))
        # result = func(*args, **kwargs)
        # return result
        # return 'running inner() {} {}'.format(func.__name__, func(*args, **kwargs))
        print('running inner() {} {}'.format(func.__name__, func(*args, **kwargs)))
        return func(*args, **kwargs)
    return inner

#@deco
def target(x):
    return 'running target():{}'.format(x)
    # print('running target()')

if __name__ == '__main__':
    #target()
    deco(target)(2)
    #print(target())
    # print(deco(target(2)))
    #print(deco(target)())