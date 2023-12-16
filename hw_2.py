class Employee:
    def __init__(self, name: str, salary_for_day: float):
        self.name = name
        self.salary_for_day = salary_for_day

    def work(self) -> str:
        return f"I come to the office."

    def __str__(self) -> str:
        return f"Position: {self.__class__.__name__}, name: {self.name}"

    def __gt__(self, other):
        return self.salary_for_day > other.salary_for_day

    def __lt__(self, other):
        return self.salary_for_day < other.salary_for_day

    def __le__(self, other):
        return self.salary_for_day <= other.salary_for_day

    def __ge__(self, other):
        return self.salary_for_day >= other.salary_for_day

    def __eq__(self, other):
        return self.salary_for_day == other.salary_for_day

    def __ne__(self, other):
        return self.salary_for_day != other.salary_for_day


class Recruiter(Employee):

    def work(self) -> str:
        return f"I come to the office and start to hiring."


class Developer(Employee):
    def __init__(self, name: str, salary_for_day: float, tech_stack: list):
        super().__init__(name, salary_for_day)
        self.tech_stack = tech_stack

    def work(self) -> str:
        return f"I come to the office and start to coding."

    def __gt__(self, other):
        return self.tech_stack > other.tech_stack

    def __lt__(self, other):
        return self.tech_stack < other.tech_stack

    def __eq__(self, other):
        return self.tech_stack == other.tech_stack

    def __ge__(self, other):
        return self.tech_stack >= other.tech_stack

    def __le__(self, other):
        return self.tech_stack <= other.tech_stack


d1 = Developer("Stan", 5000, ['Python'])
d2 = Developer("Eric", 6000, ['Rust', 'Dart'])
print(d2 > d1)
print(d2 != d1)
print(d2 <= d1)






