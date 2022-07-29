#Упражнение 81. Двоичное число в десятичное (с учетом дробных чисел).

number = input("Введите число в двоичном виде: ")
number_0 = []
number_list = list(number) # преобразуем введенное число в список
if ',' in number_list:
    index = number_list.index(',')
    #Далее разбиваем с помощью срезов список на два списка
    number_list_L = number_list[0:index:1]
    number_list_R = number_list[index+1::1]
    reverse_number_list_L = number_list_L[::-1] #с помощью среза переворачиваем список
    #далее преобразуем список в список целочисленных значений
    for i, item in enumerate(reverse_number_list_L):
        reverse_number_list_L[i] = int(item)
    for i, item in enumerate(number_list_R):
        number_list_R[i] = int(item)
    for x in range(0, len(reverse_number_list_L)):
        number_0.append(reverse_number_list_L[x]*(2**x))
    for x in range(0, len(number_list_R)):
        number_0.append(number_list_R[x]*(2**(-(x+1))))
    print("Введенное число в десятичном виде:", sum(number_0))
else:
    number_list = list(number)  # преобразуем введенное число в список
    reverse_number_list = number_list[::-1]  # с помощью среза переворачиваем список
    # далее преобразуем список в список целочисленных значений
    for i, item in enumerate(reverse_number_list):
        reverse_number_list[i] = int(item)
    for x in range(0, len(reverse_number_list)):
        number_0.append(reverse_number_list[x] * (2 ** x))
    print("Введенное число в десятичном виде:", sum(number_0))