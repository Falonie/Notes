def fuc(name, gender, **kwargs):
    print('name:', name, 'gender:', gender, kwargs)


def fuc1(*args, **kwargs):
    print('args', args)
    print('kw', kwargs)


def fuc2(name, gender, **kw):
    print('name:', name, 'gender:', gender, kw)


def fuc3(name, age, nationality='Chinese', *args, **kwargs):
    print('name:', name, 'age:', age, 'nationality:', nationality, args, kwargs)


if __name__ == '__main__':
    fuc(name='Caseny', gender='male')
    fuc1(2, 3, 4, gender='female')
    fuc2('Caseny', 'male', city='zhoushan')
    fuc3('Caseny', 26)
    fuc3('Caseny', 26, 'Japanese', 123, 'ABC', ds='ew')