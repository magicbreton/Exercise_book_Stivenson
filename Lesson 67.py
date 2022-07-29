#Упражнение 67. Найти периметр многоугольника
all_x=[] #формируем пустой список для х
all_y=[] #формируем пустой список для y
side_lengths=[] #формируем пустой список длин сторон многоугольника
koordinate_x = input("Введите первую координату Х: ")
koordinate_y = input("Введите первую координату Y: ")
#Начало цикла, пока сообщение не станет пустым
while koordinate_x !="":
    all_x.append(koordinate_x) #добавляем каждое введенное значение в список all_x
    all_y.append(koordinate_y)  # добавляем каждое введенное значение в список all_y
    koordinate_x = input("Введите следующую координату Х (Enter для окончания ввода): ")
    if koordinate_x =="":
        break
    koordinate_y = input("Введите следующую координату Y: ")

print(all_x)
print(all_y)
#Преобразовываем спиком состаящий из строк, в список значений с плавающей точкой
all_x_float=[float(x) for x in all_x]
all_y_float=[float(y) for y in all_y]
print(all_x_float)
print(all_y_float)

if len(all_y_float)>2:
    #Разность межжду соседними элементами списка:
    xdiff=[all_x_float[n]-all_x_float[n-1] for n in range(1,len(all_x_float))]
    ydiff = [all_y_float[n] - all_y_float[n - 1] for n in range(1,len(all_y_float))]
    #Список длин; map(lambda (x,y): x+y, zip(list1, list2))
    side_lengths=list(map(lambda x,y: (x**2+y**2)**0.5, xdiff,ydiff))
    #Разность между первым и последним элементом списка
    xdiff_1_max=[all_x_float[0]-all_x_float[-1]]
    ydiff_1_max = [all_y_float[0] - all_y_float[-1]]
    #расстояние между первой и последней точкой
    side_lengths_1_max=list(map(lambda x,y: (x**2+y**2)**0.5, xdiff_1_max, ydiff_1_max))
    #определение всех расстояний (вывод с список)
    all_lengths=side_lengths+side_lengths_1_max
print("Разность соседних элементов списка х: ", xdiff)
print("Разность соседних элементов списка y: ", ydiff)
print("Разность между первым и последним элементом списка х: ", xdiff_1_max)
print("Разность между первым и последним элементом списка y: ", ydiff_1_max)
print("Список длин: ", side_lengths)
print("Расстояние между первой и последней точкой: ", side_lengths_1_max)
print("Все расстояния: ", all_lengths)
print("Периметр многоугольника равен ", sum(all_lengths))