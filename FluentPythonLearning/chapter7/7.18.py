from clockdeco2 import clock
import functools,time

@functools.lru_cache()
@clock
def fibonacci(n):
    t0 = time.time()
    # result = n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)
    if n < 2:
        result = n
    elif n >= 2:
        result = fibonacci(n - 2) + fibonacci(n - 1)
    t = time.time() - t0
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)
    # return result

if __name__ == '__main__':
    fibonacci(10)
