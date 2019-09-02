class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __getattr__(self, item):
        # if item:
        if item not in ('day', 'month', 'year'):
            #     raise ValueError('No such attribute!')
            return "attribute's name is {}".format(item)

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day=day, month=month, year=year)
        return date1

    @staticmethod
    def is_date_valid(data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999
        # return day,month,year

    def is_date_valid2(self, data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    def __repr__(self):
        return 'day {} month {} year {}'.format(self.day, self.month, self.year)

    def __str__(self):
        return 'day {} month {} year {}'.format(self.day, self.month, self.year)

    def output(self):
        return self.day, self.month, self.year


if __name__ == '__main__':
    date3 = Date(1, 1, 2018)
    print(date3.day)
    print(date3.age)