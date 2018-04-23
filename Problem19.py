# Solution without using built in Datetime module

class Date:
    def __init__(self, day, month, year, dayOfWeek):
        self.day = day
        self.month = month
        self.year = year
        self.dayOfWeek = dayOfWeek

    def daysInMonth(self):
        if self.month in [9, 4, 6, 11]:
            return 30
        # Febuary special case
        if self.month == 2:
            if self.leapYear():
                return 29
            else:
                return 28
        return 31

    def leapYear(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        return False

    def getDate(self):
        return [self.day, self.month, self.year]

    def tomorrow(self):
        self.day += 1
        if self.day > self.daysInMonth():
            self.day -= self.daysInMonth()
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month -= 12

        # 0 is Monday and 6 is Sunday
        self.dayOfWeek += 1
        self.dayOfWeek %= 7


date = Date(1, 1, 1900, 0)

# Iterate until we are at the beginning date of 1 Jan 1901
while date.getDate() != [1, 1, 1901]:
    date.tomorrow()

# Iterate to 31 Dec 2000 and count the Sundays
sundays = 0
while date.getDate() != [31, 12, 2000]:
    if date.day == 1 and date.dayOfWeek == 6:
        sundays += 1
    date.tomorrow()

print(sundays)