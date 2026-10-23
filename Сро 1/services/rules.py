from abc import ABC, abstractmethod


class EligibilityRule(ABC):
    @abstractmethod
    def check(self, course, study_plan):
        pass


class CreditsRule(EligibilityRule):
    def __init__(self, max_credits=30):
        self.max_credits = max_credits

    def check(self, course, study_plan):
        current_credits = study_plan.total_credits
        new_total = current_credits + course.credits

        if new_total > self.max_credits:
            return False, (
                f"Превышен лимит кредитов: "
                f"{new_total} > {self.max_credits}"
            )

        return True, ""


class PrerequisiteRule(EligibilityRule):
    def check(self, course, study_plan):
        completed = study_plan.completed_courses
        registered = {
            registered_course.course_id
            for registered_course in study_plan.courses
        }

        missing = [
            prerequisite
            for prerequisite in course.prerequisites
            if prerequisite not in completed
            and prerequisite not in registered
        ]

        if missing:
            return False, (
                "Не выполнены пререквизиты: "
                + ", ".join(missing)
            )

        return True, ""


class ScheduleRule(EligibilityRule):
    def check(self, course, study_plan):
        for registered_course in study_plan.courses:
            conflicts = (
                set(course.schedule)
                & set(registered_course.schedule)
            )

            if conflicts:
                return False, (
                    "Конфликт расписания: "
                    + ", ".join(sorted(conflicts))
                )

        return True, ""


class CompositeRule:
    def __init__(self, rules):
        self.rules = list(rules)

    def check(self, course, study_plan):
        errors = []

        for rule in self.rules:
            allowed, message = rule.check(course, study_plan)

            if not allowed:
                errors.append(message)

        return len(errors) == 0, errors 