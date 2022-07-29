#Упражнение 65. Таблица соотношения температур

from prettytable import PrettyTable #импортируем установленный модуль

table = PrettyTable()
#определяем шапку и данные
table.field_names = ['Температура в градусах Цельсия, C', 'Температура по Фаренгейту, F']
temp_Celsey = {x: x for x in range(0, 110, 10)}
temp_Farengeyt = {i: (i*1.8+32) for i in temp_Celsey}
for i in temp_Celsey and temp_Farengeyt:
    table.add_row(["%.2f" % (temp_Celsey[i]), "%.2f" % (temp_Farengeyt[i])])

print(table)