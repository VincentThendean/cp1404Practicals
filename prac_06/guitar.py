"""
Guitars
Estimate: 60 minutes
Start: 15:49
Finish: 16:28
Actual: 39 minutes
"""

import datetime


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = str(name)
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        today = datetime.date.today()
        year = today.year-1

        return year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False


