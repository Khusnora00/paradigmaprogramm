def procedural_registration(student_name, course_name, registered_courses):
    if not student_name or not course_name:
        return False, "Не указано имя или название дисциплины"

    if course_name in registered_courses:
        return False, "Студент уже записан на эту дисциплину"

    registered_courses.append(course_name)
    return True, f"{student_name} зарегистрирован на дисциплину {course_name}"


class Student:
    def _init_(self, name, group=""):
        self.name = name
        self.group = group
        self.registered_courses = []

    def register_course(self, course_name):
        if not self.name or not course_name:
            return False, "Не указано имя или название дисциплины"

        if course_name in self.registered_courses:
            return False, "Студент уже записан на эту дисциплину"

        self.registered_courses.append(course_name)
        return True, f"{self.name} зарегистрирован на дисциплину {course_name}"


def main():
    print("=" * 45)
    print("СРАВНЕНИЕ ПАРАДИГМ ПРОГРАММИРОВАНИЯ")
    print("=" * 45)

    courses = []
    success, message = procedural_registration(
        "Хуснора",
        "Искусственный интеллект",
        courses,
    )
    print("\nПроцедурный подход:")
    print(message)
    print("Дисциплины:", courses)

    student = Student("Хуснора", "ТИИ 25-21")
    success, message = student.register_course("Искусственный интеллект")
    print("\nОбъектно-ориентированный подход:")
    print(message)
    print("Группа:", student.group)
    print("Дисциплины:", student.registered_courses)

    print("\nПроцедурный подход использует функции и отдельные данные.")
    print("ООП объединяет данные и методы в объектах.")


if __name__ == "__main__":
    main() 