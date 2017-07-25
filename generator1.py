# #print([x*x for x in list(range(100))])
# a=(x*x for x in list(range(100)))
#
# print(next(a))
# print(a.__next__())
#
# for b in a:
#     print(b)

def main():
    for i in list(range(1, 101)):
        yield i ** 2

if __name__ == '__main__':
    print(main().__next__(), next(main()), next(main()))
    for i in main():
        print(i)