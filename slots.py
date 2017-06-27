class Employee(object):
    def set_salary(self,salary):
        self.salary=salary
        n=Employee()
        Employee.set_salary=set_salary
        n.set_salary(15000)
print(n.salary)