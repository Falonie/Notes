import random

class AbstractShape(object):
    def __init__(self, color):
        self.color = color

class Circle(AbstractShape):
    def __init__(self, color=None, r=.0):
        # super().__init__(color)
        super(Circle, self).__init__(color)
        self.r = r

    def __repr__(self):
        return 'Color is {},radius is {r:.8f}.'.format(self.color, r=self.r)

if __name__ == '__main__':
    c = Circle()
    c.color = 'blue'
    c.r = random.random()
    print(c)