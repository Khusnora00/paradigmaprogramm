def procedural_registration(student_name, course_name, registered_courses):
    if not student_name or not course_name:
        return False, "Не указано имя или название дисциплины"

    if course_name in registered_courses:
        return False, "Студент уже записан на эту дисциплину"

    registered_courses.append(course_name)
    return True, student_name + " зарегистрирован на дисциплину " + course_name


class Student:
    def __init__(self, name):
        self.name = name
        self.registered_courses = []

    def register_course(self, course_name):
        if not self.name or not course_name:
            return False, "Не указано имя или название дисциплины"

        if course_name in self.registered_courses:
            return False, "Студент уже записан на эту дисциплину"

        self.registered_courses.append(course_name)
        return True, self.name + " зарегистрирован на дисциплину " + course_name


def main():
    print("=" * 45)
    print("СРАВНЕНИЕ ПАРАДИГМ ПРОГРАММИРОВАНИЯ")
    print("=" * 45)

    print("\n1. ПРОЦЕДУРНЫЙ ПОДХОД")

    courses = []
    success, message = procedural_registration(
        "Хуснора",
        "Искусственный интеллект",
        courses
    )

    print(message)
    print("Список дисциплин:", courses)

    print("\n2. ОБЪЕКТНО-ОРИЕНТИРОВАННЫЙ ПОДХОД")

    student = Student("Хуснора")
    success, message = student.register_course("Искусственный интеллект")

    print(message)
    print("Список дисциплин:", student.registered_courses)

    print("\n3. СРАВНЕНИЕ")
    print("Процедурный подход использует функции и отдельные данные.")
    print("ООП объединяет данные и методы внутри объектов.")
    print("Оба подхода решают одну задачу разными способами.")


if __name__ == "__main__":
    main() 