import unittest
from hw_5 import Recruiter


class TestRecruiter(unittest.TestCase):
    def test_recruiter_creation(self):
        recruiter = Recruiter(name='Eric', salary_for_day=150.0)
        self.assertEqual(recruiter.name, 'Eric')
        self.assertEqual(recruiter.salary_for_day, 150.0)


if __name__ == '__main__':
    unittest.main()
