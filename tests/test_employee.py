import unittest
from hw_5 import Employee
from email_exceptions import EmailAlreadyExistsException


class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        employee = Employee(name="Yurii", salary_for_day=200.0, email='yurii@gmail.com')
        self.assertEqual(employee.name, "Yurii")
        self.assertEqual(employee.salary_for_day, 200.0)
        self.assertEqual(employee.email, 'yurii@gmail.com')

    def test_email_validation(self):
        existing_email = "add_here_existing@gmail.com"
        with open('emails.csv', 'w') as f:
            f.write(f"{existing_email}")

        with self.assertRaises(EmailAlreadyExistsException) as e:
            employee = Employee(name='Stan', salary_for_day=250, email=existing_email)
            employee.validate()

        self.assertEqual(str(e.exception), f"Email '{existing_email}' already exists.")


if __name__ == '__main__':
    unittest.main()
