class Foo_public(object):
    bar = 123

    def __init__(self, bob):
        self.bob = bob


print(Foo_public.bar)
foo_public = Foo_public(456)
print(foo_public.bob)
print()


class Foo_protected(object):
    _bar = 123

    def __init__(self, bob):
        self._bob = bob


class Son(Foo_protected):
    def print_bob(self):
        return self._bob

    @classmethod
    def print_bar(cls):
        return cls._bar


print(Son.print_bar())
son = Son(456)
print(son.print_bob())
print(son._bar, Son._bar, son._bob, Son._bar)
print()


class Private(object):
    __bar = 123

    def __init__(self, bob):
        self.__bob = bob


class Private_Son(Private):
    def print_bob(self):
        return self.__bob

    @classmethod
    def print_bar(cls):
        return cls.__bar


# print(Private_Son.__bar) #ERROR
# print(Private_Son.__bob) #ERROR
son = Private_Son(456)
# print(son.__bob) #ERROR
# print(son.__bar) #ERROR
# print(Private._Private__bar)
