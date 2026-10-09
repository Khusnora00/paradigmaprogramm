from .repository import Repository


class AttendanceService:
    """Сервис управления посещаемостью студентов."""

    def __init__(self, repository: Repository):
        self._repository = repository

    def record_attendance(
        self,
        student_id: int,
        attendance: bool,
    ) -> None:
        """Сохраняет отметку посещаемости."""
        self._validate_student_id(student_id)

        if not isinstance(attendance, bool):
            raise TypeError(
                "Отметка посещаемости должна быть True или False"
            )

        self._repository.save(student_id, attendance)

    def get_attendance(self, student_id: int) -> list[bool]:
        """Возвращает историю посещаемости студента."""
        self._validate_student_id(student_id)
        return self._repository.get(student_id)

    @staticmethod
    def _validate_student_id(student_id: int) -> None:
        """Проверяет идентификатор студента."""
        if isinstance(student_id, bool) or not isinstance(student_id, int):
            raise TypeError(
                "Идентификатор студента должен быть целым числом"
            )

        if student_id <= 0:
            raise ValueError(
                "Идентификатор студента должен быть положительным"
            )
