class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x * self.y

    def bar(self):
        return self.x

    @classmethod
    def obj(cls, x, y):
        return cls(x, y)

    @staticmethod
    def obj2():
        return 'static'

    def __str__(self):
        return "{} {},{}".format(self.__class__.__name__, self.x, self.y)

c = Point(2, 3)
print(c.get())
print(Point(3,4))
print(Point.obj(4,4))
print(Point.obj2())
