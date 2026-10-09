from .calculations import calculate_scholarship
from .report import format_decision


def main():
    average = 85
    social_category = "льготная"

    amount = calculate_scholarship(
        average,
        social_category,
    )

    decision = format_decision(
        average,
        social_category,
        amount,
    )

    print(decision)


if __name__ == "__main__":
    main() 