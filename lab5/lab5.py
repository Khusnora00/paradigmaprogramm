class Student:
    """Представляет студента и хранит его оценки."""
    def __init__(self, student_id, name, group):
        """Создаёт студента после проверки входных данных."""
        if isinstance(student_id, bool) or not isinstance(student_id, int):
            raise TypeError("Идентификатор должен быть целым числом")
        if student_id <= 0:
            raise ValueError("Идентификатор должен быть положительным")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя не должно быть пустым")
        if not isinstance(group, str) or not group.strip():
            raise ValueError("Группа не должна быть пустой")
        self.student_id = student_id
        self.name = name.strip()
        self.group = group.strip()
        self._scores = []
    def add_score(self, score):
        """Добавляет оценку после проверки её корректности."""
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("Балл должен быть числом")
        if not 0 <= score <= 100:
            raise ValueError("Балл должен быть от 0 до 100")
        self._scores.append(float(score))
    @property
    def scores(self):
        """Возвращает неизменяемый список оценок."""
        return tuple(self._scores)
    @property
    def average(self):
        """Вычисляет средний балл студента."""
        if not self._scores:
            return None
        return sum(self._scores) / len(self._scores)
    @property
    def status(self):
        """Возвращает статус допуска студента."""
        if self.average is None:
            return "нет данных"
        if self.average >= 50:
            return "допущен"
        return "не допущен"
    def __repr__(self):
        """Возвращает краткое представление студента."""
        return (
            f"Student(student_id={self.student_id!r}, "
            f"name={self.name!r}, group={self.group!r})"
        )

    
class GradeBook:
    """Хранит список студентов."""

    def __init__(self):
        """Создаёт журнал студентов."""
        self._students = {}

    def register(self, student):
        """Регистрирует студента."""
        if not isinstance(student, Student):
            raise TypeError("Можно регистрировать только студентов")

        if student.student_id in self._students:
            raise ValueError("Студент уже зарегистрирован")

        self._students[student.student_id] = student

    def find(self, student_id):
        """Находит студента по ID."""
        if student_id not in self._students:
            raise KeyError("Студент не найден")

        return self._students[student_id]

    def ranking(self):
        """Возвращает рейтинг студентов по среднему баллу."""
        return sorted(
            self._students.values(),
            key=lambda student: (
                student.average is None,
                -(student.average if student.average is not None else 0)
            )
        )
    
class Payment:
    """Представляет платёж."""

    def __init__(self, operation, amount):
        """Проверяет данные платежа."""
        if operation not in ("начисление", "оплата"):
            raise ValueError("Неизвестный тип операции")

        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")

        self.operation = operation
        self.amount = float(amount)

    def __repr__(self):
        return f"Payment(operation={self.operation!r}, amount={self.amount!r})"
   

class StudentAccount:
    """Счёт студента."""

    def __init__(self, student_name):
        """Создаёт счёт студента."""
        if not isinstance(student_name, str) or not student_name.strip():
            raise ValueError("Имя студента не должно быть пустым")

        self.student_name = student_name
        self.balance = 0.0

    def charge(self, amount):
        """Начисляет деньги на счёт."""
        payment = Payment("начисление", amount)
        self.balance += payment.amount

    def pay(self, amount):
        """Списывает деньги со счёта."""
        payment = Payment("оплата", amount)

        if payment.amount > self.balance:
            raise ValueError("Недостаточно средств")

        self.balance -= payment.amount 