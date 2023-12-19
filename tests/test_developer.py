import unittest
from hw_5 import Developer


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


if __name__ == '__main__':
    unittest.main()

