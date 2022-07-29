#Упражнение 66. Никаких центов
#Запрашиваем у пользователя цену в долларах
price = input("Введите цену: ")
all_price=[] #формируем пустой список

#Начало цикла, пока сообщение не станет пустым
while price !="":
    all_price.append(price) #добавляем каждое введенное значение в список

    #Запрашиваем у пользователя цену
    price = input("Введите цену, $: ")
# преобразуем список из строковых элементов в список из элементов с плавающей точкой
float_price = [float(x) for x in all_price]
print("Сумма всех введенных сумм: ", sum(float_price), "$")
sum_float_price_cent = 100 * sum(float_price)  # сумма центов
if 100 * sum(float_price) % 5 < 2.5:
    print("Сумма, которую покупатель должен заплатить наличными: ", (100 * sum(float_price) // 5) * 0.05, "$")
else:
    print("Сумма, которую покупатель должен заплатить наличными: ",
              "%.2f" % ((100 * sum(float_price) // 5 + 1) * 0.05), "$")