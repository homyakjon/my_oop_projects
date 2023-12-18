from hw_5 import Employee
from email_exceptions import EmailAlreadyExistsException

employee = Employee(name="Yurii", salary_for_day=200.0)
a = Employee(name="Stan", salary_for_day=300.0)
days_to_check = 10
salary_result = employee.check_salary(days=days_to_check)
print(f"Зарплата за {days_to_check} рабочих дней: {salary_result}")

employee.email = 'yurii@gmail.com'
try:
    employee.validate()
    print("Email успешно добавлен.")
except EmailAlreadyExistsException as e:
    print(f"Ошибка: {e}")

a.email = 'hello@gmail.com'
try:
    a.validate()
    print("Email успешно добавлен.")
except EmailAlreadyExistsException as e:
    print(f"Ошибка: {e}")
