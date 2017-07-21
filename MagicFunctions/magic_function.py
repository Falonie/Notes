class Function(object):
    def __init__(self, *args):
        if args is None:
            self.values = []
        else:
            self.values = list(args)

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

if __name__ == '__main__':
    a = Function(2, 3, 'we')
    # print(Function({'name':'caren'}))