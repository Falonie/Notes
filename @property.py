class Screen(object):
    @property
    def fuc(self):
        return self._width

    @fuc.setter
    def fuc(self, width):
        # if not isinstance(width,int):
        #   raise ValueError('Error')
        self._width = width

    @property
    def fuc2(self):
        return self._height

    @fuc2.setter
    def fuc2(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.fuc = 1980
s.fuc2 = 1080
print(s.resolution)

class Screen2(object):
    def f(self, width):
        self.width = width

    def g(self, height):
        self.height = height

    def r(self):
        return self.width * self.height

    def __repr__(self):
        return '{} * {} = {}'.format(self.width, self.height, self.width * self.height)

a = Screen2()
a.width = 1600
a.height = 900
print(a.r())
print(a)