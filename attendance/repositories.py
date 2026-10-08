import json

class DictRepository:
    """Хранилище посещаемости на основе словаря."""

    def __init__(self):
        self._data = {}

    def save(self, student_id: int, attendance: bool) -> None:
        """Сохраняет отметку посещаемости."""
        self._data.setdefault(student_id, []).append(attendance)

    def get(self, student_id: int) -> list[bool]:
        """Возвращает отметки посещаемости."""
        return self._data.get(student_id, []).copy()

class FileRepositoryStub:
    """Файловое хранилище посещаемости."""

    def __init__(self, filename: str):
        self._filename = filename

    def save(self, student_id: int, attendance: bool) -> None:
        """Сохраняет отметку в JSON-файл."""
        data = self._read()

        key = str(student_id)
        data.setdefault(key, []).append(attendance)

        self._write(data)

    def get(self, student_id: int) -> list[bool]:
        """Возвращает отметки из JSON-файла."""
        data = self._read()
        return data.get(str(student_id), []).copy()

    def _read(self) -> dict:
        """Читает данные из файла."""
        try:
            with open(
                self._filename,
                "r",
                encoding="utf-8",
            ) as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write(self, data: dict) -> None:
        """Записывает данные в файл."""
        with open(
            self._filename,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4,
            )

class MemorySpy:
    """Тестовое хранилище, отслеживающее обращения."""

    def __init__(self):
        self._data = {}
        self.saved = []
        self.requested = []

    def save(self, student_id: int, attendance: bool) -> None:
        """Сохраняет отметку и записывает вызов."""
        self.saved.append((student_id, attendance))
        self._data.setdefault(student_id, []).append(attendance)

    def get(self, student_id: int) -> list[bool]:
        """Возвращает отметки и записывает запрос."""
        self.requested.append(student_id)
        return self._data.get(student_id, []).copy()
