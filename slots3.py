class Employee(object):
    __slots__ = ('name', 'salary')


n = Employee()
n.name = 'Caren'
n.salary = 18000
# n.age = 26
print(n.name, n.salary)