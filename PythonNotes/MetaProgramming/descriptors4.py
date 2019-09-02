class M(object):
    # def __init__(self, x=1):
    #     self.x = x

    def __set_name__(self, owner, name=1):
        print('name {}'.format(name))
        self.x = name

    def __get__(self, instance, owner):
        print(f"get: {instance}, {owner}")
        # return self.x
        return instance.__dict__[self.x]

    def __set__(self, instance, value):
        print(f"set: {instance}, {value}")
        # self.x = value
        instance.__dict__[self.x] = value


class X:
    m = M()


x = X()
print(x.m)
x.m = 10
print(x.m)
