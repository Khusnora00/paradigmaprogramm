from .rating import build_rating, filter_students
from .report import format_report


def main():
    """Запускает программу обработки экзаменационной ведомости."""

    students = [
        {"id": 101, "name": "Amina", "scores": [88, 92, 79]},
        {"id": 102, "name": "Dias", "scores": [45, 52, 48]},
        {"id": 103, "name": "Mira", "scores": []},
    ]

    rating = build_rating(students, pass_mark=50)

    print("Экзаменационная ведомость")
    print(format_report(rating))

    admitted = filter_students(students, threshold=50)

    print("\nСтуденты, прошедшие порог:")
    print(format_report(admitted))


if __name__ == "__main__":
    main() 