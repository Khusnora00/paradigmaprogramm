
import re
import sqlite3

# Исходные данные
students = [
    {'name': 'Aida', 'group': 'IS-24-01', 'score': 82, 'attendance': 91, 'email': 'aida@atu.edu.kz'},
    {'name': 'Miras', 'group': 'IS-24-01', 'score': 69, 'attendance': 88, 'email': 'miras@atu.edu.kz'},
    {'name': 'Dana', 'group': 'IS-24-02', 'score': 91, 'attendance': 96, 'email': 'dana@atu.edu.kz'},
    {'name': 'Timur', 'group': 'IS-24-02', 'score': 74, 'attendance': 62, 'email': 'timur_at_atu.kz'},
    {'name': 'Aliya', 'group': 'IS-24-03', 'score': 87, 'attendance': 79, 'email': 'aliya@atu.edu.kz'},
    {'name': 'Arman', 'group': 'IS-24-03', 'score': 55, 'attendance': 72, 'email': 'arman@atu.edu.kz'}
]

print("========== ЗАДАНИЕ 1 ==========")

# Императивный стиль
passed_imperative = []

for student in students:
    if student['score'] >= 75:
        passed_imperative.append(student['name'])

# Декларативный стиль
passed_declarative = [
    student['name']
    for student in students
    if student['score'] >= 75
]

print("Императивный результат:", passed_imperative)
print("Декларативный результат:", passed_declarative)
print("Результаты совпадают:", passed_imperative == passed_declarative)


print("\n========== ЗАДАНИЕ 2 ==========")

has_excellent = any(s['score'] >= 90 for s in students)
all_attended = all(s['attendance'] >= 60 for s in students)

average = (
    sum(s['score'] for s in students) / len(students)
    if students else 0
)

print("Есть отличник:", has_excellent)
print("Посещаемость всех не ниже 60%:", all_attended)
print("Средний балл:", round(average, 1))

# Проверяем, как изменится all при посещаемости ниже 60%
students[3]['attendance'] = 55

all_attended_changed = all(
    s['attendance'] >= 60 for s in students
)

print("После изменения посещаемости:", all_attended_changed)

# Возвращаем исходное значение
students[3]['attendance'] = 62


print("\n========== ЗАДАНИЕ 3 ==========")

group_pattern = r'^[A-Z]{2}-\d{2}-\d{2}$'
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_groups = [
    s['group'] for s in students
    if not re.fullmatch(group_pattern, s['group'])
]

invalid_emails = [
    s['email'] for s in students
    if not re.fullmatch(email_pattern, s['email'])
]

print("Ошибочные группы:", invalid_groups)
print("Ошибочные email:", invalid_emails)

# Исправляем неправильный адрес электронной почты
students[3]['email'] = 'timur@atu.edu.kz'

invalid_emails = [
    s['email'] for s in students
    if not re.fullmatch(email_pattern, s['email'])
]

print("Email после исправления:", invalid_emails)


print("\n========== ЗАДАНИЕ 4 ==========")

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE students (
    name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    score INTEGER NOT NULL,
    attendance INTEGER NOT NULL,
    email TEXT NOT NULL
)
''')

rows = [
    (s['name'], s['group'], s['score'], s['attendance'], s['email'])
    for s in students
]

cursor.executemany(
    'INSERT INTO students VALUES (?, ?, ?, ?, ?)',
    rows
)

connection.commit()

print("Таблица students успешно создана.")
print("Количество записей:", len(rows))


print("\n========== ЗАДАНИЕ 5 ==========")

print("\nВыборка и сортировка:")

query = '''
SELECT name, score, attendance
FROM students
WHERE score >= 75 AND attendance >= 70
ORDER BY score DESC
'''

for row in cursor.execute(query):
    print(row)


print("\nГруппировка и агрегирование:")

query = '''
SELECT group_name,
       COUNT(*) AS student_count,
       ROUND(AVG(score), 1) AS average_score
FROM students
GROUP BY group_name
HAVING AVG(score) >= 70
ORDER BY average_score DESC
'''

for row in cursor.execute(query):
    print(row)


print("\n========== ЗАДАНИЕ 6 ==========")

query = '''
SELECT name, group_name, score, email
FROM students
WHERE score >= 70 AND attendance >= 70
ORDER BY score DESC
'''

result = cursor.execute(query).fetchall()

valid_result = [
    row for row in result
    if re.fullmatch(email_pattern, row[3])
]

print("Рейтинг допущенных студентов:")

for place, row in enumerate(valid_result, start=1):
    name, group_name, score, email = row
    print(f"{place}. {name} | {group_name} | {score} | {email}")


print("\n========== ИНДИВИДУАЛЬНОЕ ЗАДАНИЕ ==========")

# Активные студенты: посещаемость от 85%, оценка от 60
active_students = [
    s['name']
    for s in students
    if s['attendance'] >= 85 and s['score'] >= 60
]

print("Активные студенты:", active_students)

# Проверяем наличие оценки не ниже 90
has_high_score = any(
    s['score'] >= 90 for s in students
)

print("Есть студент с оценкой не ниже 90:", has_high_score)

connection.close()

print("\n========== ПРОГРАММА ЗАВЕРШЕНА ==========")
