class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


class Slaughter_Muslim:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            a = self.data[self.index]
            return a
        self.index += 1


if __name__ == '__main__':
    a = Counter(3, 8)
    for c in a:
        print(c)
    r = Reverse('slaughter Muslim')
    print(list(r))
    s = Slaughter_Muslim('slaughter Muslim')
    print(list(s))

# g = (x ** 2 for x in range(10))
# print(g.__next__())
# for a in g:
#     print(a)
# print('slaughter Muslim'[5])