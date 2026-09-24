import unittest

from university_rating.calculations import (
    calculate_average,
    determine_status,
)
from university_rating.rating import build_rating
from university_rating.validation import validate_scores, validate_student


class RatingTests(unittest.TestCase):

    def test_empty_average(self):
        self.assertIsNone(calculate_average([]))

    def test_empty_students(self):
        self.assertEqual(build_rating([]), [])

    def test_empty_scores(self):
        students = [
            {"id": 1, "name": "Mira", "scores": []}
        ]

        result = build_rating(students)

        self.assertIsNone(result[0]["average"])
        self.assertEqual(result[0]["status"], "нет данных")

    def test_status_boundary(self):
        self.assertEqual(determine_status(49.99), "не допущен")
        self.assertEqual(determine_status(50), "допущен")

    def test_zero_score(self):
        self.assertEqual(validate_scores([0]), [0.0])

    def test_hundred_score(self):
        self.assertEqual(validate_scores([100]), [100.0])

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            validate_scores([80, 101])

    def test_negative_score(self):
        with self.assertRaises(ValueError):
            validate_scores([-1])

    def test_string_score(self):
        with self.assertRaises(TypeError):
            validate_scores(["80"])

    def test_boolean_score(self):
        with self.assertRaises(TypeError):
            validate_scores([True])

    def test_missing_name(self):
        with self.assertRaises(ValueError) as context:
            validate_student({
                "id": 1,
                "scores": [80],
            })

        self.assertIn("name", str(context.exception))

    def test_source_is_not_changed(self):
        students = [
            {"id": 1, "name": "Test", "scores": [70, 80]}
        ]

        before = [
            {"id": 1, "name": "Test", "scores": [70, 80]}
        ]

        build_rating(students)

        self.assertEqual(students, before)

    def test_rating_is_sorted_descending(self):
        students = [
            {"id": 1, "name": "Low", "scores": [40, 50]},
            {"id": 2, "name": "High", "scores": [90, 100]},
            {"id": 3, "name": "Middle", "scores": [70, 80]},
            {"id": 4, "name": "No data", "scores": []},
        ]

        result = build_rating(students)

        self.assertEqual(
            [row["name"] for row in result],
            ["High", "Middle", "Low", "No data"],
        )

    def test_equal_averages_have_stable_order(self):
        students = [
            {"id": 1, "name": "First", "scores": [80, 80]},
            {"id": 2, "name": "Second", "scores": [70, 90]},
            {"id": 3, "name": "Third", "scores": [60, 100]},
        ]

        result = build_rating(students)

        self.assertEqual(
            [row["name"] for row in result],
            ["First", "Second", "Third"],
        )


if __name__ == "__main__":
    unittest.main()
