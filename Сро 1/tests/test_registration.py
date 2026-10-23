import unittest

from models.course import Course
from services.registration import (
    StudyPlan,
    calculate_credits,
    check_course,
    register_course,
    create_default_rules,
    format_study_plan,
)


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.catalog = [
            Course("1", "Основы Python", 5, [], ["Пн-09:00"]),
            Course("2", "Алгоритмы", 5, ["1"], ["Вт-09:00"]),
            Course("3", "Базы данных", 4, [], ["Пн-09:00"]),
            Course("4", "Машинное обучение", 20, [], ["Ср-09:00"]),
        ]

        self.study_plan = StudyPlan(
            "Тестовый студент",
            "123",
            completed_courses=[],
            student_group="ТИИ 25-21",
        )

        self.rules = create_default_rules(max_credits=30)

    def test_student_group(self):
        self.assertEqual(self.study_plan.student_group, "ТИИ 25-21")

    def test_calculate_credits(self):
        self.study_plan.add_course(self.catalog[0])
        self.assertEqual(calculate_credits(self.study_plan.courses), 5)

    def test_calculate_credits_empty(self):
        self.assertEqual(calculate_credits([]), 0)

    def test_register_course_success(self):
        result = register_course(
            self.catalog, self.study_plan, "1", self.rules
        )
        self.assertTrue(result["success"])
        self.assertEqual(len(self.study_plan.courses), 1)

    def test_unknown_course(self):
        result = register_course(
            self.catalog, self.study_plan, "999", self.rules
        )
        self.assertFalse(result["success"])

    def test_duplicate_course(self):
        register_course(self.catalog, self.study_plan, "1", self.rules)
        result = register_course(
            self.catalog, self.study_plan, "1", self.rules
        )
        self.assertFalse(result["success"])

    def test_prerequisite_required(self):
        result = register_course(
            self.catalog, self.study_plan, "2", self.rules
        )
        self.assertFalse(result["success"])

    def test_prerequisite_completed(self):
        self.study_plan = StudyPlan(
            "Тестовый студент",
            "123",
            completed_courses=["1"],
            student_group="ТИИ 25-21",
        )
        result = register_course(
            self.catalog, self.study_plan, "2", self.rules
        )
        self.assertTrue(result["success"])

    def test_schedule_conflict(self):
        register_course(self.catalog, self.study_plan, "1", self.rules)
        result = register_course(
            self.catalog, self.study_plan, "3", self.rules
        )
        self.assertFalse(result["success"])

    def test_credit_limit(self):
        register_course(self.catalog, self.study_plan, "4", self.rules)
        register_course(self.catalog, self.study_plan, "1", self.rules)

        extra_course = Course(
    "5",
    "Дополнительный курс",
    10,
    [],
    ["Чт-11:00"],
) 
        self.catalog.append(extra_course)

        result = register_course(
            self.catalog, self.study_plan, "5", self.rules
        )

        self.assertFalse(result["success"])
        self.assertEqual(len(self.study_plan.courses), 2)

    def test_credit_limit_boundary(self):
        register_course(self.catalog, self.study_plan, "4", self.rules)
        register_course(self.catalog, self.study_plan, "1", self.rules)

        result = register_course(
            self.catalog, self.study_plan, "2", self.rules
        )

        self.assertTrue(result["success"])
        self.assertEqual(self.study_plan.total_credits, 30)

    def test_failed_registration_does_not_add_course(self):
        result = register_course(
            self.catalog, self.study_plan, "999", self.rules
        )
        self.assertFalse(result["success"])
        self.assertEqual(len(self.study_plan.courses), 0)

    def test_format_study_plan(self):
        register_course(self.catalog, self.study_plan, "1", self.rules)
        text = format_study_plan(self.study_plan)
        self.assertIn("Основы Python", text)


if __name__ == "__main__":
    unittest.main() 