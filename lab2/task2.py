# Ввод данных
price = float(input("Цена одного товара: "))
quantity = int(input("Количество товаров: "))
discount_percent = float(input("Процент скидки: "))

# Расчёт стоимости
total_price = price * quantity
discount = total_price * discount_percent / 100
final_price = total_price - discount

# Вывод результата
print("Стоимость без скидки:", total_price)
print("Размер скидки:", discount)
print("К оплате:", final_price) 