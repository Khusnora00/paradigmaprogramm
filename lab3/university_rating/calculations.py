from .validation import validate_score


def calculate_average(scores):
    """Вычисляет средний балл студента."""

    checked = [validate_score(score) for score in scores]

    if not checked:
        return None

    return sum(checked) / len(checked)


def determine_status(average, pass_mark=50):
    """Определяет статус допуска по среднему баллу."""

    if isinstance(pass_mark, bool) or not isinstance(
        pass_mark, (int, float)
    ):
        raise TypeError("Порог должен быть числом")

    if not 0 <= pass_mark <= 100:
        raise ValueError("Порог должен быть от 0 до 100")

    if average is None:
        return "нет данных"

    return "допущен" if average >= pass_mark else "не допущен" 