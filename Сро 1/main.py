from services.registration import (
    StudyPlan,
    load_catalog,
    find_course,
    register_course,
    create_default_rules,
    format_study_plan,
)


def show_catalog(catalog):
    """Выводит каталог дисциплин."""
    print("\n========== КАТАЛОГ ДИСЦИПЛИН ==========")

    for course in catalog:
        prerequisites = (
            ", ".join(course.prerequisites)
            if course.prerequisites
            else "Нет"
        )

        print(
            f"{course.course_id} | {course.name} | "
            f"{course.credits} кредитов | "
            f"Пререквизиты: {prerequisites} | "
            f"Расписание: {', '.join(course.schedule)}"
        )


def show_student(study_plan):
    """Выводит информацию о студенте."""
    print("\n========== ДАННЫЕ СТУДЕНТА ==========")
    print(f"ФИО: {study_plan.student_name}")
    print(f"Номер студента: {study_plan.student_id}")


def select_course(catalog, study_plan, rules):
    """Обрабатывает запрос на регистрацию."""
    course_id = input(
        "\nВведите ID дисциплины для регистрации: "
    ).strip().upper()

    result = register_course(
        catalog,
        study_plan,
        course_id,
        rules,
    )

    if result["success"]:
        course = find_course(catalog, course_id)
        print(f"\nРегистрация успешна: {course.name}")
    else:
        print("\nВ регистрации отказано.")
        print("Причины:")

        for reason in result["reasons"]:
            print(f"- {reason}")


def show_study_plan(study_plan):
    """Показывает индивидуальный учебный план."""
    print("\n========== ИНДИВИДУАЛЬНЫЙ УЧЕБНЫЙ ПЛАН ==========")
    print(format_study_plan(study_plan))


def show_credits(study_plan):
    """Показывает количество кредитов."""
    print("\n========== КРЕДИТЫ ==========")
    print(f"Выбрано дисциплин: {len(study_plan.courses)}")
    print(f"Всего кредитов: {study_plan.total_credits}")


def show_menu():
    """Показывает главное меню."""
    print(
        "\n========== РЕГИСТРАЦИЯ СТУДЕНТОВ ==========\n"
        "1. Показать каталог дисциплин\n"
        "2. Показать данные студента\n"
        "3. Зарегистрироваться на дисциплину\n"
        "4. Показать индивидуальный учебный план\n"
        "5. Показать количество кредитов\n"
        "0. Выход"
    )


def main():
    """Точка входа в программу."""
    try:
        catalog = load_catalog()
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Ошибка загрузки каталога: {error}")
        return

    student_name = input("Введите ФИО студента: ").strip()

    while not student_name:
        print("ФИО не может быть пустым.")
        student_name = input("Введите ФИО студента: ").strip()

    student_id = input("Введите номер студента: ").strip()

    while not student_id:
        print("Номер студента не может быть пустым.")
        student_id = input("Введите номер студента: ").strip()

    study_plan = StudyPlan(
        student_name,
        student_id,
        completed_courses=[],
    )

    rules = create_default_rules(max_credits=30)

    print(f"\nДобро пожаловать, {student_name}!")

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_catalog(catalog)

        elif choice == "2":
            show_student(study_plan)

        elif choice == "3":
            select_course(catalog, study_plan, rules)

        elif choice == "4":
            show_study_plan(study_plan)

        elif choice == "5":
            show_credits(study_plan)

        elif choice == "0":
            print("Работа программы завершена.")
            break

        else:
            print("Неверный пункт меню. Попробуйте снова.")


if __name__ == "__main__":
    main() 