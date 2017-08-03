# print([x * x for x in list(range(100))])
# a = (x * x for x in list(range(100)))
#
# print(next(a))
# print(a.__next__())
#
# for b in a:
#     print(b)


def main():
    for i in list(range(1, 20)):
        yield i ** 2

def _odd_iter(n):
    n = 1
    while n < 50:
        yield n
        n = n + 2

if __name__ == '__main__':
    print(main().__next__(), next(main()), next(main()))
    for i in main():
        print(i)
    print(_odd_iter(10).__next__())
    for i in _odd_iter(10):
        print(i)


# comparison between generator and non-generator

def fib(n):
    a, b = 0, 1
    while a < n:
        # a, b = b, a + b
        yield a
        a, b = b, a + b


def fib1(n):
    a, b = 0, 1
    result = []
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


if __name__ == '__main__':
    # print(fib(10).__next__(), next(fib(10)), next(fib(10)))
    # print(fib1(10))
    # for i in fib(10):
    #     print(i)
    pass