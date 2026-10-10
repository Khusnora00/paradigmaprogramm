# Список оценок студентов
scores = [95, 82, 67, 45, 91, 76, 54, 88, 40, 73]

# Счётчики оценок
count_A = 0
count_B = 0
count_C = 0
count_F = 0

# Подсчёт оценок
for score in scores:
    if score >= 90 and score <= 100:
        count_A = count_A + 1
    elif score >= 75:
        count_B = count_B + 1
    elif score >= 50:
        count_C = count_C + 1
    elif score >= 0:
        count_F = count_F + 1

# Вывод результатов
print("Количество оценок A:", count_A)
print("Количество оценок B:", count_B)
print("Количество оценок C:", count_C)
print("Количество оценок F:", count_F) 