class Employee(object):
    def __init__(self,salary):
        self._salary=salary
    def __call__(self):
        print('My salary is %s' % self._salary)
n=Employee(15000)
print(n())
print(n.__call__())