class Employee(object):
    def set_salary(self, salary):
        self.salary = salary

n = Employee()
n.set_salary(15000)
print(n.salary)