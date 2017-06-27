class Employee(object):
    salary=14000
n=Employee()
n.salary=15000
print(n.salary)
print(Employee.salary)

class Company(object):
    group='Alibaba'
g=Company()
g.group='Google'
print(g.group,Company.group)