import unittest
from hw_6 import Developer


class TestDeveloper(unittest.TestCase):
    def test_developer_creation(self):
        developer = Developer(name='Kenny', salary_for_day=200.0, tech_stack=["Python", "JavaScript"])
        self.assertEqual(developer.name, 'Kenny')
        self.assertEqual(developer.salary_for_day, 200.0)
        self.assertEqual(developer.tech_stack, ["Python", "JavaScript"])

    def test_add_method(self):
        dev1 = Developer(name="Kenny", salary_for_day=200.0, tech_stack=["Python", "JavaScript"])
        dev2 = Developer(name="Kyle", salary_for_day=140.0, tech_stack=["JavaScript", "HTML"])

        new_dev = dev1 + dev2

        self.assertEqual(new_dev.name, "Kenny + Kyle")
        self.assertEqual(new_dev.salary_for_day, 200.0)
        self.assertCountEqual(new_dev.tech_stack, ["Python", "JavaScript", "HTML"])

    def setUp(self):
        self.prog1 = Developer("Kenny", 200.0, ["Python", "JavaScript"])
        self.prog2 = Developer("Bob", 150.0, ["Python", "Java", "C++"])
        self.prog3 = Developer("Kyle", 140.0, ["Python", "Java"])

    def test_greater_than(self):
        self.assertTrue(self.prog2 > self.prog1)
        self.assertFalse(self.prog1 > self.prog2)

    def test_less_than(self):
        self.assertTrue(self.prog1 < self.prog2)
        self.assertFalse(self.prog2 < self.prog1)

    def test_equal(self):
        self.assertTrue(self.prog1 == self.prog3)
        self.assertFalse(self.prog1 == self.prog2)

    def test_greater_than_or_equal(self):
        self.assertTrue(self.prog2 >= self.prog1)
        self.assertTrue(self.prog1 >= self.prog3)
        self.assertFalse(self.prog1 >= self.prog2)

    def test_less_than_or_equal(self):
        self.assertTrue(self.prog1 <= self.prog3)
        self.assertTrue(self.prog1 <= self.prog2)
        self.assertFalse(self.prog2 <= self.prog1)


if __name__ == '__main__':
    unittest.main()

