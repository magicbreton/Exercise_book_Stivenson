#Упражнение 48. Знаки зодиака.
month=str(input("Введите название месяца: "))
day=int(input("Введите число: "))
if (month in ['декабрь'] and (day>=22 and day<=31)) or (month in ['январь'] and (day>=1 and day<=19)):
    print("Козерог.")
elif (month in ['январь'] and (day>=20 and day<=31)) or (month in ['февраль'] and (day>=1 and day<=18)):
    print("Водолей.")
elif (month in ['февраль'] and (day>=19 and day<=28)) or (month in ['март'] and (day>=1 and day<=20)):
    print("Рыбы.")
elif (month in ['март'] and (day>=21 and day<=31)) or (month in ['апрель'] and (day>=1 and day<=19)):
    print("Овен.")
elif (month in ['апрель'] and (day>=20 and day<=30)) or (month in ['май'] and (day>=1 and day<=20)):
    print("Телец.")
elif (month in ['май'] and (day>=21 and day<=31)) or (month in ['июнь'] and (day>=1 and day<=20)):
    print("Близнецы.")
elif (month in ['июнь'] and (day>=21 and day<=30)) or (month in ['июль'] and (day>=1 and day<=22)):
    print("Рак.")
elif (month in ['июль'] and (day>=23 and day<=31)) or (month in ['август'] and (day>=1 and day<=22)):
    print("Лев.")
elif (month in ['август'] and (day>=23 and day<=31)) or (month in ['сентябрь'] and (day>=1 and day<=22)):
    print("Дева.")
elif (month in ['сентябрь'] and (day>=23 and day<=30)) or (month in ['октябрь'] and (day>=1 and day<=22)):
    print("Весы.")
elif (month in ['октябрь'] and (day>=23 and day<=31)) or (month in ['ноябрь'] and (day>=1 and day<=21)):
    print("Скорпион.")
elif (month in ['ноябрь'] and (day>=22 and day<=30)) or (month in ['декабрь'] and (day>=1 and day<=21)):
    print("Стрелец.")