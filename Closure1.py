def knights(saying):
    def inner(quote):
        return f'We are the knights who say {quote}'
    return inner(saying)


print(knights('Hi!'))


def knights(saying):
    def inner():
        return f'We are the knights who say {saying}'
    return inner


print(knights('Hi!')())


def adder(x):
    def wrapper(y):
        return x + y
    return wrapper


print(adder(4)(5))


def outer():
    g = 2

    def inner():
        nonlocal g
        g = 4
        print('inner }', g)
    inner()
    print('outer', g)


outer()
