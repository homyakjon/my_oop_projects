from datetime import datetime, timedelta
import csv
from email_exceptions import EmailAlreadyExistsException
import requests
from io import StringIO
import logging


class Employee:
    def __init__(self, name: str, salary_for_day: float, email: str = None):
        self.name = name
        self.salary_for_day = salary_for_day
        self.email = email
        self.validate()
        self.save_email()

    def validate(self):
        with open('emails.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            existing_emails = set(row[0] for row in reader if row)

        if self.email in existing_emails:
            error_message = f"Email '{self.email}' already exists."
            self.log_error(error_message)
            raise EmailAlreadyExistsException(error_message)

    def save_email(self):
        with open('emails.csv', 'a') as file:
            file.write(f"{self.email}\n")

    def log_error(self, error_message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('error_logs.txt', 'a') as error_file:
            error_file.write(f"{timestamp} | {error_message}\n")
        logging.error(f"{timestamp} | {error_message}")

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

    def add_email(self, email):
        self.email = email
        try:
            self.validate()
            self.save_email()
            print("Email successfully added.")
        except EmailAlreadyExistsException as e:
            print(f"Error: {e}")

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


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name_str(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, source):
        candidates_list = []

        if source.startswith('http'):
            file_content = cls.read_candidates_from_url(source)
        else:
            file_content = cls.read_candidates_from_file(source)

        reader = csv.DictReader(file_content)

        for row in reader:
            candidate = cls(
                first_name=row['Full Name'].split(' ')[0],
                last_name=row['Full Name'].split(' ')[1],
                email=row['Email'],
                tech_stack=row['Technologies'].split('|'),
                main_skill=row['Main Skill'],
                main_skill_grade=row['Main Skill Grade']
            )
            candidates_list.append(candidate)

        return candidates_list

    @classmethod
    def read_candidates_from_file(cls, file_path):
        with open(file_path, 'r', newline='') as file:
            return file

    @classmethod
    def read_candidates_from_url(cls, url):
        response = requests.get(url)
        file_content = StringIO(response.text)
        return file_content


source_path_or_url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
candidates_list = Candidate.generate_candidates(source_path_or_url)

for candidate in candidates_list:
    print(f"{candidate.full_name_str}: {candidate.email}, {candidate.tech_stack},"
          f" {candidate.main_skill}, {candidate.main_skill_grade}")







