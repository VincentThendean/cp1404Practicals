"""
Programming languages
Estimate: 60 minutes
Start: 14:56
Finish: 15:15
Actual: 19 minutes
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = str(name)
        self.typing = str(typing)
        self.reflection = bool(reflection)
        self.year = int(year)

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"

