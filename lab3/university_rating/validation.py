def validate_score(score):
    """Проверяет корректность одного балла."""

    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Балл должен быть числом")

    if not 0 <= score <= 100:
        raise ValueError("Балл должен быть от 0 до 100")

    return float(score)


def validate_student(student):
    """Проверяет данные одного студента."""

    if not isinstance(student, dict):
        raise TypeError("Студент должен быть словарём")

    student_id = student.get("id")
    name = student.get("name")
    scores = student.get("scores", [])

    if isinstance(student_id, bool) or not isinstance(student_id, int):
        raise TypeError("Идентификатор должен быть целым числом")

    if student_id <= 0:
        raise ValueError("Идентификатор должен быть положительным")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Имя не может быть пустым")

    if not isinstance(scores, (list, tuple)):
        raise TypeError("Баллы должны быть списком или кортежем")

    for score in scores:
        validate_score(score)

    return True 