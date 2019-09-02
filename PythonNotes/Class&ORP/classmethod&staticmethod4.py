import time


class Date(object):
    def __init__(self, year, month, day):
        self.day = day
        self.month = month
        self.year = year

    # @staticmethod
    # def now():
    #     t = time.localtime()
    #     return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(year=t.tm_year, month=t.tm_mon, day=t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    # def __repr__(self):
    #     return f"{self.day}, {self.month}, {self.year}"


a = Date(2018, 7, 18)
print(Date.now())
print(Date.tomorrow())
print()


class EuropeDate(Date):
    def __repr__(self):
        return f"{self.day}, {self.month}, {self.year}"


print(EuropeDate.now())
print()


class Times(object):
    factor = 1

    @classmethod
    def mul(cls, x):
        return cls.factor * x


class TwoTimes(Times):
    factor = 2


print(TwoTimes.mul(4))
