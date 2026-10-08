import os
import tempfile
import unittest

from attendance.cached_repository import CachedRepository
from attendance.repositories import (
    DictRepository,
    FileRepositoryStub,
    MemorySpy,
)
from attendance.service import AttendanceService


class AttendanceServiceTests(unittest.TestCase):
    """Проверяет работу сервиса посещаемости."""

    def test_save_and_get_attendance(self):
        """Сервис сохраняет и возвращает посещаемость."""
        repository = DictRepository()
        service = AttendanceService(repository)

        service.record_attendance(1, True)
        service.record_attendance(1, False)

        self.assertEqual(
            service.get_attendance(1),
            [True, False],
        )

    def test_unknown_student_returns_empty_list(self):
        """Для неизвестного студента возвращается пустой список."""
        service = AttendanceService(DictRepository())

        self.assertEqual(
            service.get_attendance(999),
            [],
        )

    def test_invalid_student_id_type(self):
        """Неверный тип ID вызывает TypeError."""
        service = AttendanceService(DictRepository())

        with self.assertRaises(TypeError):
            service.record_attendance("1", True)

    def test_invalid_student_id_value(self):
        """Неположительный ID вызывает ValueError."""
        service = AttendanceService(DictRepository())

        with self.assertRaises(ValueError):
            service.record_attendance(0, True)

    def test_invalid_attendance_type(self):
        """Неверный тип отметки вызывает TypeError."""
        service = AttendanceService(DictRepository())

        with self.assertRaises(TypeError):
            service.record_attendance(1, 1)

    def test_memory_spy_records_operations(self):
        """MemorySpy фиксирует обращения сервиса."""
        repository = MemorySpy()
        service = AttendanceService(repository)

        service.record_attendance(1, True)
        service.get_attendance(1)

        self.assertEqual(
            repository.saved,
            [(1, True)],
        )
        self.assertEqual(
            repository.requested,
            [1],
        )

    def test_file_repository(self):
        """FileRepositoryStub сохраняет данные в файл."""
        with tempfile.TemporaryDirectory() as directory:
            filename = os.path.join(
                directory,
                "attendance.json",
            )

            repository = FileRepositoryStub(filename)
            service = AttendanceService(repository)

            service.record_attendance(1, True)
            service.record_attendance(1, False)

            self.assertEqual(
                service.get_attendance(1),
                [True, False],
            )

    def test_cached_repository_uses_cache(self):
        """CachedRepository не обращается к хранилищу повторно."""
        repository = MemorySpy()
        cached_repository = CachedRepository(repository)
        service = AttendanceService(cached_repository)

        repository.save(1, True)

        first_result = service.get_attendance(1)
        second_result = service.get_attendance(1)

        self.assertEqual(
            first_result,
            [True],
        )
        self.assertEqual(
            second_result,
            [True],
        )
        self.assertEqual(
            repository.requested,
            [1],
        )


if __name__ == "__main__":
    unittest.main()
