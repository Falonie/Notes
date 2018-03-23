class Name(object):
    def __init__(self, name=None, name2=None, temperature=0):
        self._name = name
        self._lastname = name2
        self._temperature = temperature

    @property
    def firstname(self):
        return self._name

    @firstname.setter
    def firstname(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError('must be string')
        self._name = new_name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        if not isinstance(new_lastname, str):
            raise ValueError('must be string')
        self._lastname = new_lastname

    @property
    def fullname(self):
        # return '{} {}'.format(self._name, self._lastname)
        return '{} {}'.format(self.firstname, self.lastname)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -100 or value > 100:
            raise ValueError('new value must between -100 and 100.')
        self._temperature = value


if __name__ == '__main__':
    a = Name('Paul')
    print(a.firstname)
    a.firstname = 'LeBron'
    a.lastname = 'James'
    print(a.firstname)
    print(a.fullname)
    print(a.fullname)
    b = Name()
    b.firstname = 'Stephen'
    b.lastname = 'Curry'
    print(b.lastname)
    print(b.fullname)
    c = Name()
    c.temperature = 101
    print(c.temperature)
