class Employee(object):

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def salary_raise(self, percent):
        # return self.salary*(1+percent)
        self.salary = int(self.salary * (1 + percent))
        #self.salary = self.salary * (1 + percent)
        # self.salary *= (1 + percent)

    # def __getattr__(self, item):
    #     return self.name

    def __repr__(self):
        return '{} is {} year old.His/Her salary is ${}.'.format(self.name, self.age, self.salary)

employee_1=Employee('Bob',45,20000)
#print(employee_1)
# employee_1.salary(1)
employee_1.salary_raise(.1)
print(employee_1)
print(employee_1.__dict__)
print(employee_1.__class__.__name__)
