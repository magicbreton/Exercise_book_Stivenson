# Упражнение 50. Шкала Рихтера.
mag=float(input("Введите значение магнитуды по шкале Рихтера: "))
if mag<2:
    print("Описание землятресения: минимальное.")
elif mag>=2 and mag<3:
    print("Описание землятресения: очень слабое.")
elif mag>=3 and mag<4:
    print("Описание землятресения: слабое.")
elif mag>=4 and mag<5:
    print("Описание землятресения: промежуточное.")
elif mag>=5 and mag<6:
    print("Описание землятресения: умеренное.")
elif mag>=6 and mag<7:
    print("Описание землятресения: сильное.")
elif mag>=7 and mag<8:
    print("Описание землятресения: очень сильное.")
elif mag>=8 and mag<10:
    print("Описание землятресения: огромное.")
elif mag>=10:
    print("Описание землятресения: разрушительное.")