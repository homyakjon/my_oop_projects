from datetime import datetime, timedelta
import csv


class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name: str, salary_for_day: float):
        self.name = name
        self.salary_for_day = salary_for_day
        self.email = ''
        self.save_email()

    def save_email(self):
        with open('emails.csv', 'a', newline='') as file:
            write_file = csv.writer(file)
            write_file.writerow([self.email])

    def validate(self):
        with open('emails.csv', 'r') as file:
            reader = csv.reader(file)
            existing_emails = set(row[0] for row in reader if row)

        if self.email in existing_emails:
            raise EmailAlreadyExistsException(f"Email '{self.email}' already exists.")
        else:
            self.save_email()

    def work(self) -> str:
        return f"I come to the office."

    def check_salary(self, days):
        current_date = datetime.now()
        beginning_of_month = current_date.replace(day=1)

        working_days = 0
        current_day = beginning_of_month

        while working_days < days:
            if current_day.weekday() < 5:
                working_days += 1
            current_day += timedelta(days=1)

        return working_days * self.salary_for_day

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
    def __init__(self, name: str, salary_for_day: float):
        super().__init__(name, salary_for_day)

    def work(self) -> str:
        return f"I come to the office and start hiring."


class Developer(Employee):
    def __init__(self, name: str, salary_for_day: float, tech_stack: list):
        super().__init__(name, salary_for_day)
        self.tech_stack = tech_stack

    def work(self) -> str:
        return f"I come to the office and start coding."

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

    def __add__(self, other):
        new_name = f"{self.name} + {other.name}"
        new_tech_stack = list(set(self.tech_stack + other.tech_stack))
        new_salary = max(self.salary_for_day, other.salary_for_day)
        new_developer = Developer(new_name, new_salary, new_tech_stack)
        return new_developer


employee = Employee(name="Yurii", salary_for_day=200.0)
a = Employee(name="Stan", salary_for_day=300.0)
days_to_check = 10
salary_result = employee.check_salary(days=days_to_check)
print(f"Salary for {days_to_check} working days: {salary_result}")

employee.email = 'yurii@gmail.com'
try:
    employee.validate()
    print("Email successfully added.")
except EmailAlreadyExistsException as e:
    print(f"Error: {e}")

a.email = 'hello@gmail.com'
try:
    a.validate()
    print("Email successfully added.")
except EmailAlreadyExistsException as e:
    print(f"Error: {e}")