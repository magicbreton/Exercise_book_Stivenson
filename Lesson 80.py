#Упражнение 80. Простые множители.
import copy
n = int(input("Введите целое число (2 или больше): "))
v = copy.copy(n) #создаем поверхностную копию введенного числа
m = [] #список простых множителей (пустой)
factor = 2
if n >= 2:
    while factor <= n:
        if n%factor == 0:
            m.append(factor)
            n = n//factor
        else:
            factor += 1
    print("Простые множители числа", v,":")
    print('\n'.join(map(str, m)))
elif n < 2:
    print("Ошибка. Введенное значение меньше 2.")