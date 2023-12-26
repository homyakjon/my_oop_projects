import unittest
from datetime import datetime
from hw_6 import Employee
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

    def test_check_salary(self):
        employee = Employee(name="John Doe", salary_for_day=200)

        fixed_date = datetime(2023, 12, 31)

        expected_salary = 2000
        calculated_salary = employee.check_salary(10, start_date=fixed_date)

        self.assertEqual(calculated_salary, expected_salary)

    def setUp(self):
        self.emp1 = Employee("Alice", 100)
        self.emp2 = Employee("Bob", 150)
        self.emp3 = Employee("Charlie", 100)

    def test_greater_than(self):
        self.assertTrue(self.emp2 > self.emp1)
        self.assertFalse(self.emp1 > self.emp2)

    def test_less_than(self):
        self.assertTrue(self.emp1 < self.emp2)
        self.assertFalse(self.emp2 < self.emp1)

    def test_less_than_or_equal(self):
        self.assertTrue(self.emp1 <= self.emp3)
        self.assertTrue(self.emp1 <= self.emp2)
        self.assertFalse(self.emp2 <= self.emp1)

    def test_greater_than_or_equal(self):
        self.assertTrue(self.emp2 >= self.emp1)
        self.assertTrue(self.emp1 >= self.emp3)
        self.assertFalse(self.emp1 >= self.emp2)

    def test_equal(self):
        self.assertTrue(self.emp1 == self.emp3)
        self.assertFalse(self.emp1 == self.emp2)

    def test_not_equal(self):
        self.assertTrue(self.emp1 != self.emp2)
        self.assertFalse(self.emp1 != self.emp3)


if __name__ == '__main__':
    unittest.main()
