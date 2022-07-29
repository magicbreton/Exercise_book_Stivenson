#Упражнение 78. Гипотеза Коллатца

number = int(input("Введите число: "))

while number > 0:
    number_0 = []
    number_0.append(number)
    while number_0[len(number_0)-1] != 1:
        if (number_0[len(number_0)-1]) % 2 == 0:
            number_0.append(number_0[len(number_0)-1]//2)
        else:
            number_0.append(number_0[len(number_0) - 1]*3+1)
    print(number_0)
    number = int(input("Введите следующее число (введите число меньшее либо равное нулю для окончания ввода): "))
    if number <= 0:
        break