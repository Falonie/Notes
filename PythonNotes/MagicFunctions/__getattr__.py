class Getattr(object):
    def __getattr__(self, item):
        return


class A(Getattr):
    num = 1234

    def __init__(self, x):
        self.x = x

    def __getattribute__(self, item):
        print(f'getattribute: {item}')
        return object.__getattribute__(self, item)
        # return super().__getattribute__(item)
        # return getattr(self, item)

    def __getattr__(self, item):
        print(f'getattr: {item}')
        return self.__dict__.get(item)
        # return super().__getattr__(item)
        # return object.__dict__.get(item)

    def __setattr__(self, key, value):
        print(f'set: {key} = {value}')
        self.__dict__[key] = value


a = A(11)
print(a.num)
print(a.x)
print(a.aaa)
a.x = 100
print(a.x)
print(a.__dict__)
