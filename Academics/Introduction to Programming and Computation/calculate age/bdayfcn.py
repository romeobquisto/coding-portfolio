#ME11_2.py

class Birthday:
    def __init__(self, month, day, year):
        self.m = int(month)
        self.d = int(day)
        self.y = int(year)
    def compare(self, month, day, year):
        if month < self.m:
            return year - self.y - 1
        elif month == self.m:
            if day < self.d:
                return year - self.y - 1
            else:
                return year - self.y
        else:
            return year - self.y
