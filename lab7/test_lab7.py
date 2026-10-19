import unittest

from main import (
    validate_score,
    validate_scores,
    normalize_scores,
    average,
    student_rating,
    recursive_max,
    recursive_position,
    sort_rating,
)


class TestStudentRating(unittest.TestCase):

    def test_validate_score(self):
        self.assertEqual(validate_score(80), 80.0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            validate_score("80")

    def test_bool_is_invalid(self):
        with self.assertRaises(TypeError):
            validate_score(True)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            validate_score(120)

    def test_validate_does_not_change_source(self):
        source = [50, 80, 90]
        original = source.copy()
        validate_scores(source)
        self.assertEqual(source, original)

    def test_normalize_scores(self):
        self.assertEqual(
            normalize_scores([50, 100]),
            [0.5, 1.0],
        )

    def test_average(self):
        self.assertEqual(average([60, 80]), 70.0)

    def test_average_empty(self):
        self.assertIsNone(average([]))

    def test_student_status(self):
        self.assertEqual(
            student_rating([60, 80])["status"],
            "допущен",
        )

    def test_recursive_max(self):
        self.assertEqual(recursive_max([20, 90, 50]), 90)

    def test_recursive_max_empty(self):
        with self.assertRaises(ValueError):
            recursive_max([])

    def test_recursive_position_found(self):
        self.assertEqual(
            recursive_position([10, 20, 30], 20),
            1,
        )

    def test_recursive_position_not_found(self):
        self.assertEqual(
            recursive_position([10, 20, 30], 50),
            -1,
        )

    def test_sort_rating(self):
        students = {
            "Ali": [70, 80],
            "Amina": [90, 100],
        }
        result = sort_rating(students)

        self.assertEqual(result[0][0], "Amina")
        self.assertEqual(result[1][0], "Ali")

    def test_report_does_not_change_source(self):
        source = [70, 80, 90]
        original = source.copy()
        student_rating(source)
        self.assertEqual(source, original)


if __name__ == "_main_":
    unittest.main() 