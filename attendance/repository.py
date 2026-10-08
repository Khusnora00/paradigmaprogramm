from typing import Protocol


class Repository(Protocol):
    """Контракт хранилища посещаемости."""

    def save(self, student_id: int, attendance: bool) -> None:
        """Сохраняет отметку посещаемости."""
        ...

    def get(self, student_id: int) -> list[bool]:
        """Возвращает отметки посещаемости студента."""
        ...
