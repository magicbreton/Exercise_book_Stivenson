#Упражнение 69. Билеты в зоопарк.
ages = []#формируем пустой список
age = input("Введите возраст посетителя зоопарка: ")
while age !="":
    if float(age) < 3:
        ages.append(0.00)
    elif float(age) >= 3 and float(age) < 13:
        ages.append(14.00)
    elif float(age) > 65:
        ages.append(18.00)
    else:
        ages.append(23.00)
    age = input("Введите возраст посетителя зоопарка: ")
    if age =="":
        break
print("Общая цена билетов, $: ", "%.2f"%sum(ages))