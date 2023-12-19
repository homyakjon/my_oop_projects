import unittest
from hw_5 import Candidate


class TestCandidate(unittest.TestCase):
    def test_candidate_creation(self):
        candidate = Candidate(
            first_name="Eric",
            last_name="Cartman",
            email="erik@gmail.com",
            tech_stack=["Scala", "Java"],
            main_skill="Scala",
            main_skill_grade="Uppermediate"
        )

        self.assertEqual(candidate.first_name, "Eric")
        self.assertEqual(candidate.last_name, "Cartman")
        self.assertEqual(candidate.email, "erik@gmail.com")
        self.assertEqual(candidate.tech_stack, ["Scala", "Java"])
        self.assertEqual(candidate.main_skill, "Scala")
        self.assertEqual(candidate.main_skill_grade, "Uppermediate")


if __name__ == '__main__':
    unittest.main()

