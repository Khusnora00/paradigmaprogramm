import unittest

from models.course import Course
from services.registration import (
    StudyPlan,
    calculate_credits,
    register_course,
    create_default_rules,
    format_study_plan,
)


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.course1 = Course(
            "1", "Python", 10, [], ["Monday 09:00"]
        )
        self.course2 = Course(
            "2", "Algorithms", 10, ["1"], ["Tuesday 10:00"]
        )
        self.course3 = Course(
            "3", "Databases", 15, [], ["Wednesday 11:00"]
        )
        self.course4 = Course(
            "4", "Networks", 5, [], ["Monday 09:00"]
        )

        self.catalog = [
            self.course1,
            self.course2,
            self.course3,
            self.course4,
        ]

        self.study_plan = StudyPlan(
            "Корганбаева Хуснора", "1"
        )
        self.rules = create_default_rules(max_credits=30)

    # 1. Успешная регистрация
    def test_register_course_success(self):
        result = register_course(
            self.catalog, self.study_plan, "1", self.rules
        )

        self.assertTrue(result["success"])
        self.assertTrue(self.study_plan.contains("1"))

    # 2. Несуществующая дисциплина
    def test_unknown_course(self):
        result = register_course(
            self.catalog, self.study_plan, "999", self.rules
        )

        self.assertFalse(result["success"])
        self.assertTrue(result["reasons"])

    # 3. Повторная регистрация
    def test_duplicate_course(self):
        register_course(
            self.catalog, self.study_plan, "1", self.rules
        )

        result = register_course(
            self.catalog, self.study_plan, "1", self.rules
        )

        self.assertFalse(result["success"])
        self.assertTrue(result["reasons"])

    # 4. Отсутствующий пререквизит
    def test_prerequisite_required(self):
        result = register_course(
            self.catalog, self.study_plan, "2", self.rules
        )

        self.assertFalse(result["success"])
        self.assertTrue(result["reasons"])

    # 5. Выполненный пререквизит
    def test_prerequisite_completed(self):
        self.study_plan = StudyPlan(
            "Корганбаева Хуснора",
            "1",
            completed_courses=["1"],
        )

        result = register_course(
            self.catalog, self.study_plan, "2", self.rules
        )

        self.assertTrue(result["success"])
        self.assertTrue(self.study_plan.contains("2"))

    # 6. Превышение лимита кредитов
    def test_credit_limit(self):
        register_course(
            self.catalog, self.study_plan, "1", self.rules
        )
        register_course(
            self.catalog, self.study_plan, "2", self.rules
        )

        result = register_course(
            self.catalog, self.study_plan, "3", self.rules
        )

        self.assertFalse(result["success"])
        self.assertTrue(result["reasons"])

    # 7. Конфликт расписания
    def test_schedule_conflict(self):
        register_course(
            self.catalog, self.study_plan, "1", self.rules
        )

        result = register_course(
            self.catalog, self.study_plan, "4", self.rules
        )

        self.assertFalse(result["success"])
        self.assertTrue(result["reasons"])

    # 8. Расчёт кредитов
    def test_calculate_credits(self):
        result = calculate_credits(
            [self.course1, self.course2]
        )

        self.assertEqual(result, 20)

    # 9. Формирование учебного плана
    def test_format_study_plan(self):
        register_course(
            self.catalog, self.study_plan, "1", self.rules
        )

        result = format_study_plan(self.study_plan)

        self.assertIn("Корганбаева Хуснора", result)
        self.assertIn("1", result)
        self.assertIn("10", result)

    # 10. Расчёт кредитов для пустого списка
    def test_calculate_credits_empty(self):
        result = calculate_credits([])

        self.assertEqual(result, 0)

    # 11. Неуспешная регистрация не изменяет учебный план
    def test_failed_registration_does_not_add_course(self):
        result = register_course(
            self.catalog,
            self.study_plan,
            "999",
            self.rules,
        )

        self.assertFalse(result["success"])
        self.assertFalse(self.study_plan.contains("999"))

    # 12. Регистрация при достижении лимита ровно в 30 кредитов
    def test_credit_limit_boundary(self):
        course5 = Course(
            "5",
            "Software Testing",
            10,
            [],
            ["Friday 15:00"],
        )

        self.catalog.append(course5)

        register_course(
            self.catalog, self.study_plan, "1", self.rules
        )
        register_course(
            self.catalog, self.study_plan, "2", self.rules
        )

        result = register_course(
            self.catalog, self.study_plan, "5", self.rules
        )

        self.assertTrue(result["success"])
        self.assertEqual(self.study_plan.total_credits, 30)


if __name__ == "_main_":
    unittest.main() 