#Упражнение 85. Вычисляем длину гипотенузы.

# @param a - длина первого катета
# @param b - длина второго катета
# @return c - длина гипотенузы
def lenghtGip():
    if a >= 0 and b >= 0:
        s = (a*a+b*b)**0.5
        return print('Длина гипотенузы: ','%.2f' % s)
    else:
        print('Ошибка. Введите значения длин больше либо равные нулю.')
a = float(input('Введите длину первого катета: '))
b = float(input('Введите длину второго катета: '))
lenghtGip()


