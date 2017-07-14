from datetime import datetime
import functools
#print(datetime.now())

def now():
    print(datetime.now())
f=now
f()
print(f.__name__,'\n')

def log(func):
    def wrapper(*args, **kwargs):
        print('call %s()' % func.__name__)
        return func(*args,**kwargs)
    return wrapper
@log
def now():
    print(datetime.now())
now()
# log(now)()
print(now.__name__,'\n')

def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator
# def now():
#     print(datetime.now())
# now=log('execute')(now)
# now()
@log('execute')
def now():
    print(datetime.now())
now()
print(now.__name__,'\n')

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s()' % func.__name__)
        return func(*args, **kwargs)
    return wrapper
@log
def now():
    print(datetime.now())
now()
print(now.__name__,'\n')

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator
@log('execute')
def now():
    print(datetime.now())
now()
print(now.__name__,'\n')

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('{0} begin call {1}()'.format(text, func.__name__))
            result = func(*args, **kwargs)
            print('{0} end call {1}()'.format(text, func.__name__))
            return result
        return wrapper
    return decorator
@log('execute')
def now(a,country='China'):
    print('Current time:{0},Country:{1}'.format(a, country))
now(datetime.now())
print(now.__name__)


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, input_width):
        self._width = input_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, input_height):
        self._height = input_height

    @property
    def resolution(self):
        return self._height * self._width

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution,'\n')

def fun(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@fun
def bar(a):
    return 'time is {}.'.format(datetime.now()), a
print(bar('AAA'))
