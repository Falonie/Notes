class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day=day, month=month, year=year)
        return date1

    @staticmethod
    def is_date_valid(data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    def is_date_valid2(self, data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


if __name__ == '__main__':
    date2 = Date.from_string('11-09-2012')
    is_date = Date.is_date_valid('11-09-2012')
    print(is_date)
    date = Date()
    is_date2 = date.is_date_valid2('11-09-2012')
    print(is_date2)