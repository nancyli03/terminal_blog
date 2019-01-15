class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
    def display(self):
        return "{0}*{1}*{2}".format(self.day, self.month, self.year)


    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1


    @staticmethod
    def is_date_valid(date_as_string):
        # day, month, year = map(int, date_as_string.strip('-'))
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date1 = Date('12', '11', '2019')  # Why parameters are string instead of int?
print("This is date1: {}".format(date1))
print(date1.display())
date_string = '11-2-1999'
date2 = Date.from_string(date_string)
print("This is date2: {}".format(date2))
print(date2.display())

if Date.is_date_valid(date_string):
    print("{0} is a valid date: {1}".format(date_string, date2.display()))
else:
    print "{} is not a valid date form".format(date_string)

