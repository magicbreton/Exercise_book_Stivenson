# Упражнение 55. Длины волн видимой части спектра.
length=float(input("Введите длину волны, нм: "))
if length<380 or length>750:
    print("Введенное значение длины волны находится за пределами видимой части спектра: от 380 до 750 нм.")
elif length>=380 and length<450:
    print("Цвет: фиолетовый.")
elif length>=450 and length<495:
    print("Цвет: синий.")
elif length>=495 and length<570:
    print("Цвет: зеленый.")
elif length>=570 and length<590:
    print("Цвет: желтый.")
elif length>=590 and length<620:
    print("Цвет: оранжевый.")
elif length>=620 and length<750:
    print("Цвет: красный.")