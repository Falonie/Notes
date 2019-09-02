class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


class Employee(Person):
    def __init__(self, name, age, baseSalary):
        super(Employee, self).__init__(name, age)
        self.baseSalary = baseSalary

    def getSalary(self):
        return self.baseSalary


class Manager(Person):
    def __init__(self, name, age, baseSalary, bonus):
        super(Manager, self).__init__(name, age)
        self.baseSalary = baseSalary
        self.__bonus = bonus

    # def getSalary(self):
    #     return self.baseSalary + self.bonus
    @property
    def salary(self):
        return self.baseSalary + self.__bonus

    @salary.setter
    def salary(self, bonus):
        self.__bonus = bonus

    def __repr__(self):
        return f'name: {self.name} age:{self.age} baseSalary:{self.baseSalary} Salary:{self.salary}'


kaly = Employee("kaly", 25, 10000)
carl = Manager("carl", 30, 10000, 4000)
print(kaly.get_name(), kaly.getSalary())
# print(carl.getSalary())
print(carl.salary)
carl.salary = 2000
print(carl.salary)
print(carl)
