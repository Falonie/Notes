def fuc1(*args,**kwargs):
    print('args',args)
    print('kw',kwargs)
fuc1(2,3,4,gender='female')

def fuc(name,gender,**kwargs):
    print('name:', name, 'gender:', gender, kwargs)
fuc(name='Caseny',gender='male')

def fuc(name,gender,**kw):
    print('name:', name, 'gender:', gender, kw)
fuc('Caseny','male',city='zhoushan')

def fuc(name,age,nationality='Chinese',*args,**kwargs):
    print('name:', name, 'age:', age, 'nationality:', nationality, args, kwargs)
fuc('Caseny',26)
fuc('Caseny',26,'Japanese',123,'ABC',ds='ew')