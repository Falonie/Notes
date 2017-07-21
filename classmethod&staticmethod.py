class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


class Pizza2(object):
    radius = 40

    @classmethod
    def get_radius(cls):
        return cls.radius


if __name__ == '__main__':
    print(Pizza.get_size(Pizza(50)))
    print(Pizza(50).get_size())
    print(Pizza(50).get_size)
    m = Pizza(50).get_size()
    print(m)
    n = Pizza(50).get_size
    print(n(),'\n')

    print(Pizza2.get_radius())