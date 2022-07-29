#Упражнение 82. Десятичное число в двоичное.
import copy
q = int(input("Введите целое десятичное число: "))
q_copy = copy.copy(q)
result = ""
while q != 0:
    r = str(q%2)
    result = r +result
    q = q//2
print("Двоичное представление числа", q_copy, ":", result)