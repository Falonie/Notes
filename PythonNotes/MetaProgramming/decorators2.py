import time
import functools


def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = '{} call: {} {}'.format(text, func.__name__, text)
            print(result)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def time_elapse(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            result = 'call: {} {} {}'.format(func.__name__, func(*args, **kwargs), text)
            # func(*args,**kwargs)
            # print(result)
            return result
            # print('time elapse {}'.format(time.time()-t0))
            # return 'time elapse {}'.format(time.time() - t0)
            # return func(*args, **kwargs)
        return wrapper
    return decorator


def night(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return 'night {}'.format(result)
    return wrapper


@log('****')
@time_elapse('$$$$$')
def function(x, y):
    return x * y


# @time_elapse(text='...')
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(function(3, 4))
    # print(time_elapse('*****')(function)(3, 4))
    # print(night(time_elapse('*****')(function))(3, 4))
    # print(log('$$$$$')(time_elapse('*****')(function))(3, 5))
    # print(fib(25))
