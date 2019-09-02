class People:
    def __init__(self, name):
        self.name = name


class Employee(People):
    def __init__(self, name, department):
        super(Employee, self).__init__(name)
        self.department = department
