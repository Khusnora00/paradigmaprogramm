# Список чисел
numbers = [-4, 7, -2, 10, 5, -8]

# Императивный стиль
total = 0

for number in numbers:
    if number > 0:
        total = total + number

print("Императивный стиль:", total)

# Декларативный стиль
total = sum(number for number in numbers if number > 0)

print("Декларативный стиль:", total) 