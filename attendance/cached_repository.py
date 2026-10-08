from .repository import Repository


class CachedRepository:
    """Добавляет кеширование к любому Repository."""

    def __init__(self, repository: Repository):
        self._repository = repository
        self._cache = {}

    def save(self, student_id: int, attendance: bool) -> None:
        """Сохраняет данные и обновляет кеш."""
        self._repository.save(student_id, attendance)
        self._cache.pop(student_id, None)

    def get(self, student_id: int) -> list[bool]:
        """Возвращает данные из кеша или хранилища."""
        if student_id not in self._cache:
            self._cache[student_id] = self._repository.get(student_id)

        return self._cache[student_id].copy()
