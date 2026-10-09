def format_average(value):
    """Преобразует средний балл в строку."""
    return "—" if value is None else f"{value:.2f}"


def format_rating(rows):
    """Формирует текстовый отчёт о рейтинге."""
    lines = ["Рейтинг группы"]

    for position, row in enumerate(rows, start=1):
        average = format_average(row["average"])

        lines.append(
            f"{position}. {row['name']}: "
            f"{average} — {row['status']}"
        )

    return "\n".join(lines) 