from datetime import datetime

class Date:

    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
    
    #__str__ 
    def __str__(self):
        return f'{self.month:02d}/{self.day:02d}/{self.month}'
        

    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.year ==other.year:
            return True
        return False

    def __lt__(self, other):
        selfdate = datetime(self.year, self.month, self.day)
        otherdate = datetime(other.year, other.month, other.day)
        if selfdate < otherdate:
            return True
        return False

    def is_leap_year(self):
        
        return True if self.year % 4 == 0 and (self.year % 100 1 == 0 or self.year % 400 == 0) else False

    sample_date = Date()
    date1 = Date(1985, 5, 19)
    date2 = Date(2001, 10, 3)

    #tested with __str__
    # print(sample_date)
    # print(date1)
    # print(date2)

    #testing _eq_
    print(date1 == date2)

    #testing __It__
    print(date1 < date2)

