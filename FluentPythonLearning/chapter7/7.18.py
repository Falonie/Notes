from clockdeco2 import clock
import functools

@functools.lru_cache()
@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
    fibonacci(10)
