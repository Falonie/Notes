import time


def number(num):
    # t0 = time.time()
    lengh = len(str(num))
    list = []
    for i in range(1, lengh):
        left_num = int(str(num)[:i])
        right_num = int(str(num)[i:])
        product = left_num * right_num
        list.append(product)
    return 'maximum number:{}'.format(max(list))


def number2(num):
    # t1 = time.time()
    lenth = str(num).__len__()
    # print([int(str(num)[:i]) * int(str(num)[i:]) for i in range(1, lenth)])
    maximum_number = max([int(str(num)[:i]) * int(str(num)[i:]) for i in range(1, lenth)])
    return 'maximum number:{}'.format(maximum_number)


if __name__ == '__main__':
    print(number(2333))
    print(number2(2333))
    print(max([2, 5, 9, 0, 10]))
    print([4, 5, 2, 12, 4, 5, 4].count(4))