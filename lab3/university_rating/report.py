def format_report(rating):
    """Формирует текстовый отчёт по рейтингу студентов."""

    lines = []

    for position, student in enumerate(rating, start=1):
        average = student["average"]

        if average is None:
            average_text = "—"
        else:
            average_text = f"{average:.2f}"

        lines.append(
            f"{position}. {student['name']}: "
            f"{average_text}; {student['status']}"
        )

    return "\n".join(lines) 