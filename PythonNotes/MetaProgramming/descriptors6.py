class Grade(object):
    def __init__(self):
        # self._value = 0
        self._value = {}

    def __get__(self, instance, owner):
        # return self._value
        if instance is None:
            return self
        return self._value.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        # self._value = value
        self._value[instance] = value


class Exam(object):
    math_grade = Grade()
    science_grade = Grade()
    biology_grade = Grade()
    psychology_grade = Grade()
    physiology_grade = Grade()


exam1 = Exam()
exam1.biology_grade = 10
exam2 = Exam()
exam2.biology_grade = 100
print(exam1.biology_grade)
print(exam2.biology_grade)
