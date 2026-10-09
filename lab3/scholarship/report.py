def format_decision(average, social_category, amount):
    """Формирует решение о назначении стипендии."""
    if amount == 0:
        explanation = (
            "Средний балл ниже установленного порога. "
            "Стипендия не назначается."
        )
    else:
        explanation = (
            f"Учитывается социальная категория: {social_category}. "
            f"Размер выплаты рассчитан по установленным правилам."
        )

    return (
        f"Средний балл: {average}\n"
        f"Социальная категория: {social_category}\n"
        f"Размер стипендии: {amount} тенге\n"
        f"Объяснение: {explanation}"
    ) 