# Исходный список чисел
numbers = [12, -5, 8, -3, 21, 0, 14, -7]

# Начальные значения переменных
total = 0
positive_sum = 0
positive_count = 0
negative_count = 0
zero_count = 0

# Обработка чисел в цикле
for number in numbers:
    total = total + number

    if number > 0:
        positive_sum = positive_sum + number
        positive_count = positive_count + 1
    elif number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

# Вывод результатов
print("Сумма всех чисел:", total)
print("Сумма положительных чисел:", positive_sum)
print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)
print("Количество нулей:", zero_count) 