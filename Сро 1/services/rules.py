from abc import ABC, abstractmethod


class EligibilityRule(ABC):
    """Общий интерфейс правила регистрации."""

    @abstractmethod
    def check(self, course, study_plan):
        """Возвращает список причин отказа."""
        pass


class CreditsRule(EligibilityRule):
    """Проверяет максимальное количество кредитов."""

    def __init__(self, max_credits=30):
        self._max_credits = max_credits

    def check(self, course, study_plan):
        if study_plan.total_credits + course.credits > self._max_credits:
            return [
                f"Превышен лимит кредитов: максимум {self._max_credits}"
            ]
        return []


class PrerequisiteRule(EligibilityRule):
    """Проверяет выполненные пререквизиты."""

    def check(self, course, study_plan):
        completed = set(study_plan.completed_courses)
        selected = {item.course_id for item in study_plan.courses}

        missing = [
            prerequisite
            for prerequisite in course.prerequisites
            if prerequisite not in completed and prerequisite not in selected
        ]

        if missing:
            return [
                "Не выполнены пререквизиты: " + ", ".join(missing)
            ]
        return []


class ScheduleRule(EligibilityRule):
    """Проверяет конфликты расписания."""

    def check(self, course, study_plan):
        occupied = {
            time
            for item in study_plan.courses
            for time in item.schedule
        }

        conflicts = [
            time for time in course.schedule
            if time in occupied
        ]

        if conflicts:
            return [
                "Конфликт расписания: " + ", ".join(conflicts)
            ]
        return []


class CompositeRule(EligibilityRule):
    """Объединяет несколько правил в одно."""

    def __init__(self, rules):
        self._rules = tuple(rules)

    def check(self, course, study_plan):
        reasons = []

        for rule in self._rules:
            reasons.extend(rule.check(course, study_plan))

        return reasons 