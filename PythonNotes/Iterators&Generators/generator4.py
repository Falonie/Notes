def fibonacci(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        n += 1
        a, b = b, a + b


f = fibonacci(10)
while True:
    try:
        print(next(f))
    except StopIteration:
        break


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


f = fibonacci()
for _ in range(10):
    print(next(f))
