import json
from pathlib import Path

from models.course import Course
from services.rules import (
    CreditsRule,
    PrerequisiteRule,
    ScheduleRule,
    CompositeRule,
)


class StudyPlan:
    """Индивидуальный учебный план студента."""

    def __init__(self, student_name, student_id, completed_courses=None):
        self._student_name = student_name
        self._student_id = student_id
        self._completed_courses = tuple(completed_courses or ())
        self._courses = []

    @property
    def student_name(self):
        return self._student_name

    @property
    def student_id(self):
        return self._student_id

    @property
    def completed_courses(self):
        return self._completed_courses

    @property
    def courses(self):
        return tuple(self._courses)

    @property
    def total_credits(self):
        return sum(course.credits for course in self._courses)

    def add_course(self, course):
        """Добавляет дисциплину в учебный план."""
        if any(item.course_id == course.course_id for item in self._courses):
            return False

        self._courses.append(course)
        return True

    def contains(self, course_id):
        return any(
            course.course_id == course_id
            for course in self._courses
        )


def load_catalog(file_path=None):
    """Загружает каталог дисциплин из JSON."""
    if file_path is None:
        file_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "courses.json"
        )

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [
        Course(
            item["id"],
            item["name"],
            item["credits"],
            item["prerequisites"],
            item["schedule"],
        )
        for item in data
    ]


def find_course(catalog, course_id):
    """Находит дисциплину по идентификатору."""
    for course in catalog:
        if course.course_id == course_id:
            return course
    return None


def calculate_credits(courses):
    """Вычисляет общую сумму кредитов."""
    return sum(course.credits for course in courses)


def check_course(catalog, study_plan, course_id, rules):
    """Проверяет, можно ли зарегистрироваться на дисциплину."""
    course = find_course(catalog, course_id)

    if course is None:
        return False, ["Дисциплина не найдена в каталоге"]

    if study_plan.contains(course_id):
        return False, ["Дисциплина уже добавлена в учебный план"]

    reasons = rules.check(course, study_plan)

    return len(reasons) == 0, reasons


def register_course(catalog, study_plan, course_id, rules):
    """Регистрирует студента на выбранную дисциплину."""
    allowed, reasons = check_course(
        catalog,
        study_plan,
        course_id,
        rules,
    )

    if not allowed:
        return {
            "success": False,
            "course_id": course_id,
            "reasons": reasons,
        }

    course = find_course(catalog, course_id)
    study_plan.add_course(course)

    return {
        "success": True,
        "course_id": course_id,
        "reasons": [],
    }


def create_default_rules(max_credits=30):
    """Создаёт композицию правил регистрации."""
    return CompositeRule(
        [
            CreditsRule(max_credits),
            PrerequisiteRule(),
            ScheduleRule(),
        ]
    )


def format_study_plan(study_plan):
    """Формирует текстовое представление учебного плана."""
    lines = [
        f"Студент: {study_plan.student_name}",
        f"Номер студента: {study_plan.student_id}",
        "",
        "Выбранные дисциплины:",
    ]

    if not study_plan.courses:
        lines.append("Дисциплины пока не выбраны.")
    else:
        for course in study_plan.courses:
            lines.append(
                f"{course.course_id} | {course.name} | "
                f"{course.credits} кредитов"
            )

    lines.extend(
        [
            "",
            f"Всего кредитов: {study_plan.total_credits}",
        ]
    )

    return "\n".join(lines) 