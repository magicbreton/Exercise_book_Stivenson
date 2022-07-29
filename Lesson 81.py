#Упражнение 81. Двоичное число в десятичное.

number = input("Введите число в двоичном виде: ")
number_0 = []
number_list = list(number) # преобразуем введенное число в список
print(number_list)
reverse_number_list = number_list[::-1] #с помощью среза переворачиваем список
print(reverse_number_list)
#далее преобразуем список в список целочисленных значений
for i, item in enumerate(reverse_number_list):
    reverse_number_list[i] = int(item)
print(reverse_number_list)

for x in range(0, len(reverse_number_list)):
    number_0.append(reverse_number_list[x]*(2**x))
print(number_0)
print("Введенное число в десятичном виде:", sum(number_0))
#доработать программу, чтобы можно было вводить дробные двоичные числа.