def list_():
    global s
    for i in range(2, 33, 4):
        s = 2
        # print(i,s)
        s += i
        print(i, s)


def list2_():
    for i in range(2, 33, 4):
        print(i)


def list3_():
    global s
    for i in range(2, 33, 4):
        s = 2
        print('before {} {}'.format(i, s))
        s += i
        print('after {} {}'.format(i, s))


if __name__ == '__main__':
    # list_()
    list3_()
    pass