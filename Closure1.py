def adder(x):
    def wrapper(y):
        return x + y
    return wrapper

if __name__ == '__main__':
    a = adder(5)
    print(a(10))
    print(a(20))