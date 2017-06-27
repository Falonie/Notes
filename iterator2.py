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
            return self.current - 1

if __name__=='__main__':
    a = Counter(3, 8)
    for c in a:
        print(c)

g=(x**2 for x in range(10))
print(g.__next__())
# for a in g:
#     print(a)