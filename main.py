from hw_3 import Employee, Developer


d1 = Developer("Stan", 5000, ['Python'])
d2 = Developer("Eric", 6000, ['Rust', 'Dart'])
res_developer = d1 + d2
print(f'{res_developer.tech_stack}')
print(res_developer)
print(d2 > d1)
print(d2 != d1)
print(d2 <= d1)

employee = Employee(name="Yurii", salary_for_day=200.0)
days_to_check = 10
salary_result = employee.check_salary(days=days_to_check)
print(f"Salary for {days_to_check} working days: {salary_result}")
employee.email = 'yurii@gmail.com'
employee.validate()
employee.save_email()