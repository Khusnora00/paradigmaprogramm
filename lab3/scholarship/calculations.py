from .validation import validate_applicant


def base_amount(average):
    """Определяет базовую сумму по среднему баллу."""
    validate_applicant(average, "обычная")

    if average < 50:
        return 0
    elif average < 80:
        return 30000
    else:
        return 40000


def calculate_bonus(social_category):
    """Вычисляет дополнительную выплату."""
    if not isinstance(social_category, str):
        raise TypeError("Категория должна быть строкой")

    category = social_category.strip().lower()

    bonuses = {
        "обычная": 0,
        "льготная": 10000,
    }

    if category not in bonuses:
        raise ValueError("Неизвестная социальная категория")

    return bonuses[category]


def calculate_scholarship(average, social_category):
    """Рассчитывает итоговую стипендию."""
    validate_applicant(average, social_category)

    amount = base_amount(average)

    if amount == 0:
        return 0

    return amount + calculate_bonus(social_category) 