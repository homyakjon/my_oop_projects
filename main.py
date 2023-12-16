from hw_4 import Employee

employee = Employee(name="Yurii", salary_for_day=200.0)
emp = Employee(name="Stan", salary_for_day=300.0)

days_to_check = 10
salary_result = employee.check_salary(days=days_to_check)
print(f"Salary for {days_to_check} working days: {salary_result}")

employee.add_email('yurii@gmail.com')

emp.add_email('hello@gmail.com')
