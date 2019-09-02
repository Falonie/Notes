def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Results: ', result)
        return result
    return new_function


def square_int(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
        # return func ** 2
    return new_function


# @document_it
# @square_int
def add_ints(a, b):
    return a + b


# print(document_it(add_ints(3, 4)))
# print(document_it(add_ints)(3, 5))
# print(square_int(add_ints)(4, 5))
# print(square_int(add_ints(7, 9)))
print(document_it(square_int(add_ints))(3, 8))
# print(square_int(document_it(add_ints))(3, 8))

# print(add_ints(3, 8))
