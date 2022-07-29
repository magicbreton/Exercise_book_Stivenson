# Упражнение 54. Оценка работы.
rating=float(input("Введите рейтинг сотрудника: "))
if rating>0 and rating<0.4 or rating>0.4 and rating<0.6:
    print("Введено недопустимое значение рейтинга.")
elif rating==0.0:
    print("Низкий уровень. Прибавка ", rating*2400, "$.")
elif rating==0.4:
    print("Удовлетворительный уровень. Прибавка ", rating*2400, "$.")
elif rating>=0.6:
    print("Высокий уровень. Прибавка ", rating*2400, "$.")