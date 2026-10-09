from .validation import validate_student
from .calculations import calculate_average, determine_status


def summarize_student(student, pass_mark=50):
    """Создаёт сводную запись студента."""

    validate_student(student)

    average = calculate_average(student.get("scores", []))

    return {
        "id": student["id"],
        "name": student["name"].strip(),
        "average": average,
        "status": determine_status(average, pass_mark),
    }


def build_rating(students, pass_mark=50):
    """Формирует рейтинг студентов по среднему баллу."""

    summaries = [
        summarize_student(student, pass_mark)
        for student in students
    ]

    return sorted(
        summaries,
        key=lambda item: (
            item["average"] is not None,
            item["average"] if item["average"] is not None else 0,
        ),
        reverse=True,
    )


def filter_students(students, threshold):
    """Отбирает студентов по заданному порогу."""

    if isinstance(threshold, bool) or not isinstance(
        threshold, (int, float)
    ):
        raise TypeError("Порог должен быть числом")

    if not 0 <= threshold <= 100:
        raise ValueError("Порог должен быть от 0 до 100")

    rating = build_rating(students, pass_mark=threshold)

    return [
        student
        for student in rating
        if student["average"] is not None
        and student["average"] >= threshold
    ]