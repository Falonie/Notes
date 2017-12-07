def break_statement():
    for n in range(1, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, n // x)
                break
        else:
            print(n, 'is a prime number')


def continue_statement():
    for num in range(1, 10):
        if num % 2 == 0:
            print('Found an even number', num)
            continue
        # else:
        print('Found a number', num)


def statement():
    for i in range(2, 10):
        if i % 2 == 0:
            print('Find number:{}'.format(i))
            break
        print(i)


if __name__ == '__main__':
    break_statement()
    # print('\n')
    # continue_statement()
    # statement()
