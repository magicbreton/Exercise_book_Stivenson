month=str(input("Введите название месяца: "))
if month in ['Январь', 'январь']:
    print("В январе 31 день.")
elif month in ['Февраль', 'февраль']:
    print("В феврале может быть как 28, так и 29 дней.")
elif month in ['Март', 'март']:
    print("В марте 31 день.")
elif month in ['Апрель', 'апрель']:
    print("В апреле 30 дней.")
elif month in ['Май', 'май']:
    print("В мае 31 день.")
elif month in ['Июнь', 'июнь']:
    print("В июне 30 дней.")
elif month in ['Июль', 'июль']:
    print("В июле 31 день.")
elif month in ['Август', 'август']:
    print("В августе 31 день.")
elif month in ['Сентябрь', 'сентябрь']:
    print("В сентябре 30 дней.")
elif month in ['Октябрь', 'октябрь']:
    print("В октябре 31 день.")
elif month in ['Ноябрь', 'ноябрь']:
    print("В ноябре 30 дней.")
elif month in ['Девабрь', 'декабрь']:
    print("В декабре 31 день.")
else:
    print("Неверный ввод. Введите название месяца.")