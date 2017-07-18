class AbstractShape(object):
    def __init__(self, color):
        self.color = color

class Circle(AbstractShape):
    def __init__(self, color, r=.0):
        super().__init__(color)
        self.r = r

c=Circle