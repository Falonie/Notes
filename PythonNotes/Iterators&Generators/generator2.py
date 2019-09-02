def print_num(i):
    if i > 0:
        yield 1
    else:
        yield from print_ten()
        # print_ten()
        # yield print_ten()
        # for i in range(10):
        #     yield i


def print_ten():
    for i in range(10):
        yield i


def generate_num():
    for _ in print_num(-1):
        # for j in _:
        print(_)


# generate_num()

def myfun(total):
    for i in range(total):
        yield i
    # i = 0
    # while i < total:
    #     yield i
    #     i += 1


# for i in myfun(10):
#     print(i)
m = myfun(10)
while True:
    try:
        # print(next(m))
        print(m.send(None))
    except StopIteration:
        # print(e)
        break


def myfun2(total):
    yield from range(total)
    # for i in range(total):
    #     yield i


for i in myfun2(5):
    print('www.example.com/{}'.format(i))
