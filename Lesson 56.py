# Упражнение 56. Определение частоты.
freg=float(input("Введите частоту волны: "))
if freg<3E9:
    print("Радиоволны.")
elif freg>=3E9 and freg<3E12:
    print("Микроволны.")
elif freg>=3E12 and freg<4.3E14:
    print("Инфракрасное излучение.")
elif freg>=4.3E14 and freg<7.5E14:
    print("Видимое излучение.")
elif freg>=7.5E14 and freg<3E17:
    print("Ультрафиолетовое излучение.")
elif freg>=3E17 and freg<3E19:
    print("Рентгеновское излучение.")
elif freg>=3E19:
    print("Гамма-излучение.")