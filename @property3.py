class Name(object):

    def __init__(self, name):
        self.name = name

    @property
    def firstname(self):
        return self.name

    @firstname.setter
    def firstname(self, new_name):
        self.name = new_name

    @property
    def bar(self):
        return self.lastname

    @bar.setter
    def bar(self, new_lastname):
        self.lastname = new_lastname

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)


a = Name('Paul')
print(a.name)
print(a.firstname)
a.firstname = 'LeBron'
a.lastname = 'James'
print(a.firstname)
print(a.fullname)