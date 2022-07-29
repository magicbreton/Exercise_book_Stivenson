note=int(input("Введите номинал банкноты в долларах: "))
if note==1:
    print("Джордж Вашингтон")
elif note==2:
    print("Томас Джефферсон")
elif note==5:
    print("Авраам Линкольн")
elif note==10:
    print("Александр Гамильтон")
elif note==20:
    print("Эндрю Джексон")
elif note==50:
    print("Улисс Грант")
elif note==100:
    print("Бенджамин Франклин")
else:
    print("Ошибка. Неверный номинал банкноты.")