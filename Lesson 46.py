#Упражнение 46. Какого цвета клетка?
coor=str(input("Введите координаты клетки: "))
new_coor=list(coor)
if (new_coor[0] in ['a']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка белая.")
elif (new_coor[0] in ['a']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка черная.")
elif (new_coor[0] in ['b']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка черная.")
elif (new_coor[0] in ['b']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка белая.")
elif (new_coor[0] in ['c']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка белая.")
elif (new_coor[0] in ['c']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка черная.")
elif (new_coor[0] in ['d']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка черная.")
elif (new_coor[0]in ['d']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка белая.")
elif (new_coor[0]in ['e']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка белая.")
elif (new_coor[0] in ['e']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка черная.")
elif (new_coor[0] in ['f']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка черная.")
elif (new_coor[0] in ['f']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка белая.")
elif (new_coor[0] in ['g']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка белая.")
elif (new_coor[0] in ['g']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка черная.")
elif (new_coor[0] in ['h']) and (new_coor[1] in ['2', '4', '6', '8']):
    print("Клетка черная.")
elif (new_coor[0] in ['h']) and (new_coor[1] in ['1', '3', '5', '7']):
    print("Клетка белая.")
else:
    print("Неверный формат записи.")