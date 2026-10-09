import unittest

from scholarship.validation import validate_applicant
from scholarship.calculations import base_amount, calculate_bonus
from scholarship.report import format_decision


class TestScholarship(unittest.TestCase):

    def test_valid_applicant(self):
        self.assertTrue(validate_applicant(90, "none"))

    def test_invalid_average(self):
        with self.assertRaises(ValueError):
            validate_applicant(110, "none")

    def test_base_amount(self):
        self.assertIsInstance(base_amount(90), (int, float))

    def test_calculate_bonus(self):
        self.assertEqual(calculate_bonus("Обычная"), 0)
        self.assertEqual(calculate_bonus("Льготная"), 10000)

    def test_format_decision(self):
        result = format_decision(
            "Аmina",
            "Стипендия назначена",
            10000
        )
        self.assertIsInstance(result, str)
        self.assertIn("Стипендия назначена", result)


if __name__ == "__main__":
    unittest.main()  