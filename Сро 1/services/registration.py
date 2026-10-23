import json
from pathlib import Path

from models.course import Course
from services.rules import (
    CreditsRule,
    PrerequisiteRule,
    ScheduleRule,
    CompositeRule,
)


def calculate_credits(courses):
    """Считает общее количество кредитов."""
    return sum(course.credits for course in courses)


class StudyPlan:
    def __init__(self, student_name, student_id, completed_courses=None, student_group=""):
        self.student_name = student_name
        self.student_id = student_id
        self.student_group = student_group
        self.courses = []
        self._completed_courses = set(completed_courses or [])

    @property
    def completed_courses(self):
        return self._completed_courses.copy()

    @property
    def total_credits(self):
        return calculate_credits(self.courses)

    def contains(self, course_id):
        return any(c.course_id == str(course_id) for c in self.courses)

    def add_course(self, course):
        if self.contains(course.course_id):
            return False
        self.courses.append(course)
        return True


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

    courses = []

    for item in data:
        course = Course(
            course_id=item.get("course_id", item.get("id")),
            name=item["name"],
            credits=item["credits"],
            prerequisites=item.get("prerequisites", []),
            schedule=item.get("schedule", []),
        )
        courses.append(course)

    return courses


def find_course(catalog, course_id):
    """Находит дисциплину по ID."""
    for course in catalog:
        if course.course_id == str(course_id):
            return course

    return None


def create_default_rules(max_credits=30):
    """Создаёт стандартный набор правил."""
    return CompositeRule([
        CreditsRule(max_credits=max_credits),
        PrerequisiteRule(),
        ScheduleRule(),
    ])


def check_course(catalog, study_plan, course_id, rules):
    """Проверяет возможность регистрации."""
    course = find_course(catalog, course_id)

    if course is None:
        return False, ["Дисциплина не найдена в каталоге"]

    if study_plan.contains(course.course_id):
        return False, ["Студент уже записан на эту дисциплину"]

    return rules.check(course, study_plan)


def register_course(catalog, study_plan, course_id, rules):
    """Регистрирует студента на дисциплину."""
    course = find_course(catalog, course_id)

    if course is None:
        return {
            "success": False,
            "course_id": str(course_id),
            "reasons": ["Дисциплина не найдена в каталоге"],
        }

    if study_plan.contains(course.course_id):
        return {
            "success": False,
            "course_id": course.course_id,
            "reasons": ["Студент уже записан на эту дисциплину"],
        }

    allowed, reasons = rules.check(course, study_plan)

    if not allowed:
        return {
            "success": False,
            "course_id": course.course_id,
            "reasons": reasons,
        }

    study_plan.add_course(course)

    return {
        "success": True,
        "course_id": course.course_id,
        "reasons": [],
    }


def format_study_plan(study_plan):
    """Формирует текст индивидуального учебного плана."""
    if not study_plan.courses:
        return "Учебный план пока пуст."

    lines = []

    for course in study_plan.courses:
        lines.append(
            f"{course.course_id}. {course.name} "
            f"— {course.credits} кредитов"
        )

    lines.append(f"Всего кредитов: {study_plan.total_credits}")

    return "\n".join(lines) 