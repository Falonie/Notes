class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    # @classmethod
    # def from_string(cls, date_as_string):
    #     day, month, year = map(int, date_as_string.split('-'))
    #     date1 = cls(day=day, month=month, year=year)
    #     return date1

    @staticmethod
    def from_string(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = Date(day=day, month=month, year=year)
        return date1

    @staticmethod
    def is_date_valid(data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999
        # return day,month,year

    def is_date_valid2(self, data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    # def __repr__(self):
    #     return f'day {self.day} month {self.month} year {self.year}'

    # def __str__(self):
    #     return f'day {self.day} month {self.month} year {self.year}'

    def output(self):
        return self.day, self.month, self.year


class Date_print(Date):
    def __repr__(self):
        return f'day {self.day} month {self.month} year {self.year}'


if __name__ == '__main__':
    date2 = Date.from_string('11-09-2012')
    print(Date.from_string('11-09-2012'))
    print(Date_print.from_string('18-7-2018'))
    print(date2.output())
    print(Date.is_date_valid('11-09-2012'))
    date = Date()
    is_date2 = date.is_date_valid2('11-09-2012')
    print(is_date2)

    print(getattr(date2, 'day'), hasattr(date2, 'month'))
