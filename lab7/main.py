def validate_score(score: int | float) -> float:
    """Проверяет корректность одного балла."""
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Балл должен быть числом")

    if not 0 <= score <= 100:
        raise ValueError("Балл должен быть от 0 до 100")

    return float(score)


def validate_scores(scores: list[int | float]) -> list[float]:
    """Возвращает новый список корректных баллов."""
    return [validate_score(score) for score in scores]


def normalize_scores(
    scores: list[int | float],
) -> list[float]:
    """Нормализует баллы в диапазон от 0 до 1."""
    checked = validate_scores(scores)
    return [score / 100 for score in checked]


def average(scores: list[int | float]) -> float | None:
    """Вычисляет средний балл."""
    checked = validate_scores(scores)
    return sum(checked) / len(checked) if checked else None


def student_rating(scores: list[int | float]) -> dict:
    """Формирует рейтинг студента."""
    checked = validate_scores(scores)
    avg = average(checked)

    return {
        "scores": tuple(checked),
        "average": avg,
        "status": (
            "нет данных" if avg is None
            else "допущен" if avg >= 50
            else "не допущен"
        ),
        "maximum": recursive_max(checked) if checked else None,
    }


def recursive_max(values: list[float]) -> float:
    """Рекурсивно находит максимальный балл."""
    if not values:
        raise ValueError("Последовательность пуста")

    if len(values) == 1:
        return values[0]

    tail_max = recursive_max(values[1:])
    return values[0] if values[0] > tail_max else tail_max


def recursive_position(
    values: list[float],
    target: float,
    index: int = 0,
) -> int:
    """Рекурсивно находит позицию элемента."""
    if index >= len(values):
        return -1

    if values[index] == target:
        return index

    return recursive_position(values, target, index + 1)


def sort_rating(
    students: dict[str, list[int | float]],
) -> list[tuple[str, float]]:
    """Создаёт рейтинг студентов по среднему баллу."""
    result = [
        (name, average(scores))
        for name, scores in students.items()
    ]

    valid = [
        (name, score)
        for name, score in result
        if score is not None
    ]

    return sorted(valid, key=lambda item: item[1], reverse=True)


def main() -> None:
    """Демонстрирует работу программы."""
    students = {
        "Amina": [90, 85, 95],
        "Ali": [70, 75, 80],
        "Dana": [40, 45, 50],
    }

    for name, scores in students.items():
        print(name, student_rating(scores))

    print("Нормализация:", normalize_scores([50, 75, 100]))
    print("Рейтинг:", sort_rating(students))
    print("Позиция:", recursive_position([70, 80, 90], 80))


if __name__ == "_main_":
    main() 