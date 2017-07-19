class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def func(self):
        return ('%s,%s' % (self.__name, self.__score))

    def get1(self):
        return self.__name

    def get2(self):
        return self.__score

    def set(self, score):
        self.__score = score

if __name__ == '__main__':
    n = Student('Kate', 90)
    n.score = 95
    print(n.func())
    print(n.get1())
    print(n.get2())
    print(n.score)
    # print(n.set())