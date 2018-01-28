import functools, time


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = 'call: {}'.format(func.__name__)
        print(result)
        return func(*args, **kwargs)
    return wrapper

def log(text):
    def time_elapse(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            result = '{} call: {} {}'.format(text,func.__name__, func(*args, **kwargs))
            # func(*args,**kwargs)
            print(result)
            # return result
            # print('time elapse {}'.format(time.time()-t0))
            # return 'time elapse {}'.format(time.time() - t0)
            return func(*args, **kwargs)
        return wrapper
    return time_elapse


# @decorator
# @time_elapse
@log('start')
def function(x, y):
    return x * y


if __name__ == '__main__':
    print(function(3, 4))
