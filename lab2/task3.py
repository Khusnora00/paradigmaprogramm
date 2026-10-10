# Ввод балла
score = int(input("Введите балл от 0 до 100: "))

# Проверка балла и определение оценки
if score < 0 or score > 100:
    print("Ошибка: балл должен быть от 0 до 100")
elif score >= 90:
    print("Оценка: A")
elif score >= 75:
    print("Оценка: B")
elif score >= 50:
    print("Оценка: C")
else:
    print("Оценка: F") 