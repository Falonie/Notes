class Test:
    def __init__(self):
        self.foo = 10
        self._bar = 20
        self.__car = 30


# t = Test()
# print(t.foo, t._bar)
class Test2(Test):
    def __init__(self, foo=None):
        super().__init__()
        self.foo = foo
        # self.__car=50

    def get_car(self):
        return self.__car
    def get_bar(self):
        return self._

t=Test2()
print(t.get_car())
def external_func():
    return 23


def _internal_func():
    return 40
