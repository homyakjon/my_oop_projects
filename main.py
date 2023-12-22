from hw_5 import Employee, Recruiter, Developer, Candidate


employee1 = Employee(name="Yurii", salary_for_day=200.0)
employee2 = Employee(name="Stan", salary_for_day=300.0)
days_to_check = 10

salary_result = employee1.check_salary(days=days_to_check)
print(f"Salary for {days_to_check} working days: {salary_result}")
employee1.add_email('yurii@gmail.com')
employee2.add_email('hello@gmail.com')

recruiter = Recruiter(name='Eric', salary_for_day=150.0)

dev1 = Developer(name="Kenny", salary_for_day=200.0, tech_stack=["Python", "JavaScript"])
dev2 = Developer(name="Bob", salary_for_day=150.0, tech_stack=["Python", "Java", "C++"])
dev3 = Developer(name="Kyle", salary_for_day=140.0, tech_stack=["JavaScript", "HTML"])

candidate = Candidate(
    first_name="Eric",
    last_name="Cartman",
    email="erik@gmail.com",
    tech_stack=["Scala", "Java"],
    main_skill="Scala",
    main_skill_grade="Uppermediate"
)



