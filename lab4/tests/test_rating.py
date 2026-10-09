import unittest

from university_rating.calculations import (
    calculate_average,
    determine_status,
)
from university_rating.rating import (
    build_rating,
    filter_admitted,
)
from university_rating.validation import validate_scores


class RatingTests(unittest.TestCase):

    def test_empty_average(self):
        self.assertIsNone(calculate_average([]))

    def test_status_boundary(self):
        self.assertEqual(determine_status(49.99), "не допущен")
        self.assertEqual(determine_status(50), "допущен")

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            validate_scores([80, 101])

    def test_source_is_not_changed(self):
        students = [
            {"id": 1, "name": "Amina", "scores": [70, 80]}
        ]

        before = [
            {"id": 1, "name": "Amina", "scores": [70, 80]}
        ]

        build_rating(students)

        self.assertEqual(students, before)

    def test_filter_admitted(self):
        students = [
            {"id": 1, "name": "Amina", "scores": [80, 90]},
            {"id": 2, "name": "Dias", "scores": [30, 40]},
            {"id": 3, "name": "Mira", "scores": []},
        ]

        result = filter_admitted(students)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Amina")


if __name__ == "_main_":
    unittest.main() 