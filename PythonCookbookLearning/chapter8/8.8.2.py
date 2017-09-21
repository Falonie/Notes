class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return 'name:{}'.format(self._name)

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't not delete attribute")


class SubPerson(Person):
    @property
    # @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    # @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


if __name__ == '__main__':
    # p = Person('Falonie')
    # print(p.name)
    s = SubPerson('Falonie')
    print(s.name)
    s.name = 'Larry'
    # s.name=27
