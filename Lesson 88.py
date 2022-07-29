#Упражнение 88. Медиана трех значений.
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

def Median(a, b, c):
    median_0 = []
    median_0.append(a)
    median_0.append(b)
    median_0.append(c)
    median_0_sort = sorted(median_0)
    print('Медиана трех введенных значений равна', median_0_sort[1])
Median(a, b, c)
