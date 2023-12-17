"""
Project
Estimate: 2 hours
1)  Start: 15:30
    End: 15:51
2) Start: 18:02
Actual
"""
import datetime


class Project:

    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = import_date(start_date)
        self.priority = int(priority)
        self.cost = float(cost)
        self.completion = int(completion)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost:.2f},"
                f" completion: {self.completion}%")

    def is_complete(self):
        return self.completion == 100


def import_date(start_date):
    date_entry = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    return date_entry
