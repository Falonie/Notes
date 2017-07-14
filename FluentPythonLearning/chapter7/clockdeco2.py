import time,functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        # t0 = time.perf_counter()
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(','.join(repr(arg) for arg in args))
        elif kwargs:
            arg_lst.append('{}={}'.format(k, v) for k, v in kwargs.items())
        # print('[%.8fs]%s(%s) -> %r' % (elapsed, name, arg_str, result))
        arg_str=','.join(arg_lst)
        print('[{:.8f}]{}({}) -> {}'.format(elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def function(x, y):
    return x ** 2 + y

@clock
def function2(x,y=10):
    return x * y

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 1 else n * factorial(n - 1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling function()')
    function(3, 10)
    clock(function(3, 10))
    print('*' * 40, 'Calling factorial()')
    factorial(5)
    print('*' * 40, 'Calling function2()')
    function2(100,2)
    print('*' * 40, 'function name')
    print(function.__name__, snooze.__name__, factorial.__name__)