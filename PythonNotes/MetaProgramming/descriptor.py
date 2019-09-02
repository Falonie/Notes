class Movie(object):
    def __init__(self, title, description):
        self._title = title
        self._description = description

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError('must be string!')
        self.title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError('must be string!')
        self._description = value


# movie = Movie('Fuck', 'Fucking You!')
# print(movie.title, movie.description)
# print(type(movie.title))


class String(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('must be string!')
        instance.__dict__[self.name] = value


class Movie2(object):
    # name = String(name="The Promise")
    name = String(name=None)

    # def __init__(self, name):
    #     self.name = name

    # def __repr__(self):
    #     return f"Movie {self.name}"


s = String('Falonie')
print(s.name)
s.name = 'AAA'
print(s.name)
s.name = True
print(s.name)

# name = String(name="The Promise")
# movie = Movie2(name)
# print(movie)
instance = Movie2()
instance.name = 'The Promise'
print(instance.name)
