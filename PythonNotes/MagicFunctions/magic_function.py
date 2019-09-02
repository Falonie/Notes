class Function(object):
    def __init__(self, *args, **kwargs):
        if args is None:
            self.values = []
        else:
            self.values = list(args)

    def __call__(self, *args, **kwargs):
        return 'lists %s' % self.values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __repr__(self):
        return self.values


a = Function(2, 3, 'we', {"name": "Falonie", "age": 28, "gender": "male"})

# print(Function({'name': 'caren'}))
# print(a[1])


class Function2(object):
    def __init__(self, **kwargs):
        self.dict = kwargs

    def __getitem__(self, item):
        return self.dict[item]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]

    def __add__(self, key, other):
        self.dict[key] += other

    def __call__(self, *args, **kwargs):
        return self.dict


b = Function2(name='falonie', age=28, gender='male', score=90)
b['name'] = 'falonie wang'
b['score'] += 10
print(b())
