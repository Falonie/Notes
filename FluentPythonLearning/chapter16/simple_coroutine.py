def simple_coroutine(a):
    print('-> coroutine started:a =', a)
    b = yield a
    print('-> coroutine received:b =', b)
    c = yield a + b
    print('-> coroutine received:c =', c)


if __name__ == '__main__':
    my_coro = simple_coroutine(14)
    print(my_coro)
    next(my_coro)
    print(my_coro.send(28))
    # my_coro.send(20)
    # next(my_coro)
