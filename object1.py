class Student(object):

    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score

    # def __str__(self):
    #     return 'name:{},score:{}'.format(self.name, self.score)

    def __cmp__(self, other):
        return self.score == other

    def __add__(self, other):
        return self.score + other

    def __sub__(self, other):
        return self.score - other

    def __gt__(self, other):
        return self.score > other

    def __reversed__(self):
        return reversed(self.name)

    def __repr__(self):
        return '{}\'score is {}.'.format(self.name, self.score)

    def __getattr__(self, item):
        return self.name

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def get(self):
        return ('%s: %s,%s,%s' % (self.name, self.gender, self.score, self.get_score()))

    def get_score(self):
        return 'excellent' if self.score > 90 else 'bad'

if __name__ == '__main__':
    n = Student('Caseny', 'male', 95)
    n.name = 'Falonie'
    m = Student('Johncy', 'female', 90)
    print(n.get())
    print(n)
    print(n)
    print(n.score + 10)
    print(n.score - 5)
    print(n.score > 60)
    print(n.__dict__)
    print(n.get_score())
    print(n.name,n.gender)
    print(Student('Allen', gender=None, score=26))
    print(n.score<=m.score)