class A(object):
    def show(self):
        print('base show')


class B(A):
    def show(self):
        print('derived show')


# b = B()
# print(b.__class__)
# b.show()

class C(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, *args, **kwargs):
        print('a=', self.__a, 'b=', self.__b)


# c = C(10, 20)
# c.myprint()
# c()

class D(object):
    def fn(self):
        print('D fn')

    def __init__(self):
        print('B INIT')


class E(object):
    def fn(self):
        print('E fn')

    def __new__(cls, a):
        print('NEW', a)
        if a > 10:
            return super(E, cls).__new__(cls)

    def __init__(self, a):
        print('INIT', a)


# e1=E(5)
# e1.fn()

num = 9


def f1():
    num = 20


def f2():
    print(num)


# f2()
# f1()
# f2()
"""
9
9
"""


class F(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mydefault(self, *args):
        print('default', args)

    def __getattr__(self, item):
        return self.mydefault()


# f = F(10, 20)
