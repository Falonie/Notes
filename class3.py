class Magic(object):

    def __init__(self, values=None):
        if values is None:
            values = []
        else:
            self.values = list(values)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __repr__(self):
        return self.values

if __name__ == '__main__':
    m = Magic([1, 2, 4, 6, 4, 'wwww'])
    print(m[3])
    m[2] = '233'
    print(m[2])
    print([x for x in m])
    del m[2]
    print([x for x in m])