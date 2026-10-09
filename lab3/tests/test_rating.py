import unittest

from university_rating.validation import validate_score, validate_student
from university_rating.calculations import calculate_average
from university_rating.rating import build_rating, filter_students


class TestValidation(unittest.TestCase):

    def test_valid_score(self):
        self.assertEqual(validate_score(80), 80.0)

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            validate_score(120)

    def test_boolean_score(self):
        with self.assertRaises(TypeError):
            validate_score(True)

    def test_valid_student(self):
        student = {"id": 1, "name": "Amina", "scores": [80, 90]}
        self.assertTrue(validate_student(student))


class TestCalculations(unittest.TestCase):

    def test_average(self):
        self.assertAlmostEqual(calculate_average([80, 90]), 85.0)

    def test_empty_scores(self):
        self.assertIsNone(calculate_average([]))


class TestRating(unittest.TestCase):

    def setUp(self):
        self.students = [
            {"id": 1, "name": "Amina", "scores": [80, 90]},
            {"id": 2, "name": "Dias", "scores": [40, 50]},
            {"id": 3, "name": "Mira", "scores": []},
        ]

    def test_rating_order(self):
        rating = build_rating(self.students, pass_mark=50)
        self.assertEqual(rating[0]["name"], "Amina")
        self.assertEqual(rating[-1]["name"], "Mira")

    def test_filter_students(self):
        admitted = filter_students(self.students, threshold=50)
        names = [student["name"] for student in admitted]
        self.assertIn("Amina", names)
        self.assertNotIn("Mira", names)


if __name__ == "__main__":
    unittest.main() 