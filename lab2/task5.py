# Список оценок
scores = [67, 82, 45, 91, 76, 88, 54]

# Начальное максимальное значение
maximum = scores[0]

# Поиск максимального значения
for score in scores:
    if score > maximum:
        maximum = score

# Вывод результата
print("Максимальная оценка:", maximum) 