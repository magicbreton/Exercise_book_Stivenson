num=int(input("Введите количество сторон: "))
if num<3 or num>10:
    print("Количество сторон выходит за границу диапазона. Введите число от 3 до 10.")
else:
    if num==3:
        print("Фигура треугольник.")
    elif num==4:
        print("Фигура четырехугольник.")
    elif num==5:
        print("Фигура пятиугольник.")
    elif num==6:
        print("Фигура шестиугольник.")
    elif num==7:
        print("Фигура семиугольник.")
    elif num==8:
        print("Фигура восьмиугольник.")
    elif num==9:
        print("Фигура девятиугольник.")
    elif num==10:
        print("Фигура десятиугольник.")