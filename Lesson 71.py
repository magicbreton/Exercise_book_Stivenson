#Упражнение 71. Приблизительное число пи

#Генерируем три списка
a = [x for x in range(2, 30, 2)]
#print(a)
b = [x for x in range(3, 31, 2)]
#print(b)
c = [x for x in range(4, 32, 2)]
#print(c)
#Перемножаем элементы списков
abc = list(map(lambda x, y, z: x*y*z, a, b, c))
#print(abc)
#Каждый второй элемент списка делаем отрицательным
abc_ = list(map(lambda x: x * ((-1)**abc.index(x)), abc))
#print(abc_)
#Делим 4 на элемент списка abc_
abc_4 = list(map(lambda x: 4/x, abc_))
#print(abc_4)
abc_34=[3]+abc_4
#print(abc_34)
#От суммы элементов полной строки отнимаем сумму элементов строки, усеченной с помощью среза
for y in range(1, 16, 1):
    print("Pi (количество слагаемых равно", y, " : ", "%.15f"%(sum(abc_34)-sum(abc_34[y:])))


