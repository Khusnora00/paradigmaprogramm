from attendance.cached_repository import CachedRepository
from attendance.repositories import (
    DictRepository,
    FileRepositoryStub,
)
from attendance.service import AttendanceService


def demonstrate(repository, title):
    """Демонстрирует работу AttendanceService."""
    print(f"\n{title}")

    service = AttendanceService(repository)

    service.record_attendance(101, True)
    service.record_attendance(101, False)
    service.record_attendance(101, True)

    result = service.get_attendance(101)

    print(f"Посещаемость студента 101: {result}")


def main():
    """Запускает демонстрацию."""
    demonstrate(
        DictRepository(),
        "DictRepository",
    )

    demonstrate(
        FileRepositoryStub("attendance.json"),
        "FileRepositoryStub",
    )

    demonstrate(
        CachedRepository(DictRepository()),
        "CachedRepository",
    )


if __name__ == "__main__":
    main()
