# Упражнение 59. Следующий день.
year=int(input("Введите год: "))
month=str(input("Введите месяц: "))
day=int(input("Введите день: "))
if day==31 and month in ['декабрь', 'Декабрь']:
    print("Следующая дата: ", (year+1), "январь", "1")
if day>=1 and day<=30 and month in ['декабрь', 'Декабрь']:
    print("Следующая дата: ", year, "декабрь", (day+1))

elif day==28 and month in ['февраль', 'Февраль'] and year%4==0:
    print("Следующая дата: ", year, "февраль", "29")
elif day==28 and month in ['февраль', 'Февраль'] and year%4!=0:
    print("Следующая дата: ", year, "март", "1")
elif day==29 and month in ['февраль', 'Февраль']:
    print("Следующая дата: ", year, "март", "1")

elif day>=1 and day<31 and month in ['январь', 'Январь']:
    print("Следующая дата: ", year, "январь", (day+1))
elif day==31 and month in ['январь', 'Январь']:
    print("Следующая дата: ", year, "февраль", "1")

elif day>=1 and day<=27 and month in ['февраль', 'Февраль']:
    print("Следующая дата: ", year, "февраль", (day+1))

elif day>=1 and day<=30 and month in ['март', 'Март']:
    print("Следующая дата: ", year, "март", (day+1))
elif day==31 and month in ['март', 'Март']:
    print("Следующая дата: ", year, "апрель", "1")

elif day>=1 and day<=29 and month in ['апрель', 'Апрель']:
    print("Следующая дата: ", year, "апрель", (day+1))
elif day==30 and month in ['апрель', 'Апрель']:
    print("Следующая дата: ", year, "май", "1")

elif day>=1 and day<=30 and month in ['май', 'Май']:
    print("Следующая дата: ", year, "май", (day+1))
elif day==31 and month in ['май', 'Май']:
    print("Следующая дата: ", year, "июнь", "1")

elif day>=1 and day<=29 and month in ['июнь', 'Июнь']:
    print("Следующая дата: ", year, "июнь", (day+1))
elif day==30 and month in ['июнь', 'Июнь']:
    print("Следующая дата: ", year, "июль", "1")

elif day>=1 and day<=30 and month in ['июль', 'Июль']:
    print("Следующая дата: ", year, "июль", (day+1))
elif day==31 and month in ['июль', 'Июль']:
    print("Следующая дата: ", year, "август", "1")

elif day>=1 and day<=30 and month in ['август', 'Август']:
    print("Следующая дата: ", year, "август", (day+1))
elif day==31 and month in ['август', 'Август']:
    print("Следующая дата: ", year, "сентябрь", "1")

elif day>=1 and day<=29 and month in ['сентябрь', 'Сентябрь']:
    print("Следующая дата: ", year, "сентябрь", (day+1))
elif day==30 and month in ['сентябрь', 'Сентябрь']:
    print("Следующая дата: ", year, "октябрь", "1")

elif day>=1 and day<=30 and month in ['октябрь', 'Октябрь']:
    print("Следующая дата: ", year, "октябрь", (day+1))
elif day==31 and month in ['октябрь', 'Октябрь']:
    print("Следующая дата: ", year, "ноябрь", "1")

elif day>=1 and day<=29 and month in ['ноябрь', 'Ноябрь']:
    print("Следующая дата: ", year, "ноябрь", (day+1))
elif day==30 and month in ['ноябрь', 'Ноябрь']:
    print("Следующая дата: ", year, "декабрь", "1")