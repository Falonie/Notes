from collections import namedtuple

Result = namedtuple('Result', 'count average')
a = Result(1, 2)


# print(a)

def average():
    total = 0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / term
    return Result(count, average)


if __name__ == '__main__':
    coro_avg = average()
    next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(40))
    print(coro_avg.send(20))
    print(coro_avg.send(None))