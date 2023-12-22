import unittest
from hw_6 import Candidate
import requests
import os


class TestCandidate(unittest.TestCase):
    def test_candidate_creation(self):
        candidate = Candidate(
            first_name="Eric",
            last_name="Cartman",
            email="erik@gmail.com",
            tech_stack=["Scala", "Java"],
            main_skill="Scala",
            main_skill_grade="Uppermediate",
            salary=200.0

        )

        self.assertEqual(candidate.first_name, "Eric")
        self.assertEqual(candidate.last_name, "Cartman")
        self.assertEqual(candidate.email, "erik@gmail.com")
        self.assertEqual(candidate.tech_stack, ["Scala", "Java"])
        self.assertEqual(candidate.main_skill, "Scala")
        self.assertEqual(candidate.main_skill_grade, "Uppermediate")

    @classmethod
    def setUpClass(cls):
        url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
        response = requests.get(url)
        with open('test_candidates.csv', 'w') as file:
            file.write(response.text)

    @classmethod
    def tearDownClass(cls):
        os.remove('test_candidates.csv')

    def test_generate_candidates_from_url(self):
        candidates = Candidate.generate_candidates('test_candidates.csv')
        self.assertGreater(len(candidates), 0)
        for candidate in candidates:
            self.assertGreater(candidate.salary, 0, f"Candidate {candidate.full_name_str} has non-positive salary.")


if __name__ == '__main__':
    unittest.main()

