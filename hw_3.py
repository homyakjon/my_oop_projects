from datetime import datetime, timedelta
import csv
from email_exceptions import EmailAlreadyExistsException


class Employee:
    def __init__(self, name: str, salary_for_day: float, email: str = ''):
        self.name = name
        self.salary_for_day = salary_for_day
        self.email = ''

        if email and email.strip():
            try:
                if self.validate_email(email):
                    self.email = email
                    self.save_email()
            except EmailAlreadyExistsException as e:
                print(f"Error: {e}")

    def validate_email(self, email):
        if not email.strip():
            return False

        try:
            with open('emails.csv', 'r') as file:
                reader = csv.reader(file)
                existing_emails = set(row[0] for row in reader if row)
        except FileNotFoundError:
            existing_emails = set()

        if email in existing_emails:
            raise EmailAlreadyExistsException(f"Email '{email}' already exists.")

        return True

    def save_email(self):
        with open('emails.csv', 'a') as file:
            file.write(f"{self.email}\n")

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

    def __add__(self, other):
        new_name = f"{self.name} + {other.name}"
        new_tech_stack = list(set(self.tech_stack + other.tech_stack))
        new_salary = max(self.salary_for_day, other.salary_for_day)
        new_developer = Developer(new_name, new_salary, new_tech_stack)
        return new_developer



