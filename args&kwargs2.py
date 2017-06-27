def dict(**kwargs):
    return(kwargs)
print(dict(sex=1,score=90),'\n')

def fun2(param1, *args, **kwargs):
    print('param1 = ', param1)
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('###')
fun2(1, 2, 3, 4, a=1,b=2,c=3)

def fuc1(*args,**kw):
    print('args',args)
    print('kw',kw,'\n')
fuc1(2,3,4,gender='female')

def fuc1(*args,**kwargs):
    return args,kwargs
print(fuc1(2,3,4,gender='female'),'\n')

def fuc(x,y=0):
    return x,y
print(fuc(3),'\n')

def fuc(name,gender,**kwargs):
    return ('name:',name,'gender:',gender,kwargs)
print(fuc('Caseny','male',city='zhoushan'),'\n')

def fuc(name,age,nationality='Chinese',*args,**kwargs):
    return ('name:', name, 'age:', 'nationality:', nationality, age, args, kwargs)
print(fuc('Caseny',26),'\n')
print(fuc('Caseny',26,'Japanese',123,'ABC',ds='ew'),'\n')