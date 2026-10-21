class Course:
    """Модель университетской дисциплины."""

    def __init__(self, course_id, name, credits, prerequisites, schedule):
        if not isinstance(course_id, str) or not course_id.strip():
            raise ValueError("ID дисциплины не может быть пустым")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название дисциплины не может быть пустым")

        if (
            isinstance(credits, bool)
            or not isinstance(credits, int)
            or credits <= 0
        ):
            raise ValueError(
                "Количество кредитов должно быть положительным числом"
            )

        self._course_id = course_id
        self._name = name
        self._credits = credits
        self._prerequisites = tuple(prerequisites)
        self._schedule = tuple(schedule)

    @property
    def course_id(self):
        return self._course_id

    @property
    def name(self):
        return self._name

    @property
    def credits(self):
        return self._credits

    @property
    def prerequisites(self):
        return self._prerequisites

    @property
    def schedule(self):
        return self._schedule

    def to_dict(self):
        return {
            "id": self.course_id,
            "name": self.name,
            "credits": self.credits,
            "prerequisites": list(self.prerequisites),
            "schedule": list(self.schedule),
        }

    def _repr_(self):
        return (
            f"Course(id={self.course_id!r}, "
            f"name={self.name!r}, credits={self.credits})"
        ) 