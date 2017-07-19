class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x * self.y

    @classmethod
    def obj(cls, x, y):
        return cls(x, y)

    @staticmethod
    def obj2():
        return 'static'

if __name__ == '__main__':
    p = Point(2, 3)
    print(p.get())
    print(Point.obj(2, 3))