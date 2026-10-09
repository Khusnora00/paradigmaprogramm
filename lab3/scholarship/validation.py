def validate_applicant(average, social_category):
    """Проверяет данные заявителя."""
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise TypeError("Средний балл должен быть числом")

    if not 0 <= average <= 100:
        raise ValueError("Средний балл должен быть от 0 до 100")

    if not isinstance(social_category, str):
        raise TypeError("Социальная категория должна быть строкой")

    if not social_category.strip():
        raise ValueError("Социальная категория не может быть пустой")

    return True 