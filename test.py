from datetime import datetime

class Mobile(object):
	def __init__(self,name):
		self.name=name
a=Mobile('apple')
print(a.name)

class Mobile_2(object):
	name='Huawei'
print(Mobile_2.name)

a=list('abcde')
a='/'.join(a)
print(a)


class Foo(object):
	def __init__(self, func):
		self._func = func

	def __call__(self):
		print('class decorator runing')
		self._func()
		print('class decorator ending')

@Foo
def bar():
	print('bar')

bar()