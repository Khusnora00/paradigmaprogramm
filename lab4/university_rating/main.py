from .rating import build_rating, filter_admitted
from .report import format_rating


def load_demo_data():
    """Возвращает демонстрационные данные студентов."""
    return [
        {"id": 101, "name": "Amina", "scores": [88, 92, 79]},
        {"id": 102, "name": "Dias", "scores": [45, 52, 48]},
        {"id": 103, "name": "Mira", "scores": []},
        {"id": 104, "name": "Ali", "scores": [70, 80, 90]},
    ]


def main():
    """Запускает демонстрацию рейтинга и фильтрации."""
    students = load_demo_data()

    rating = build_rating(students)
    admitted = filter_admitted(students)

    print(format_rating(rating))
    print("\nТолько допущенные студенты:")
    print(format_rating(admitted))


if __name__ == "__main__":
    main() 