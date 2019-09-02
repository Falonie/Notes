class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print('Retrieving {}'.format(self.name))
        return self.val
        # return instance.__dict__[owner]

    def __set__(self, instance, value):
        print('Updating {}'.format(self.name))
        self.val = value


class MyClass(object):
    x = RevealAccess(10, "var 'x'")
    y = 5


m = MyClass()
print(m.x)
m.x = 50
print(m.x)
print(m.y)
print('*' * 50, '\n')
