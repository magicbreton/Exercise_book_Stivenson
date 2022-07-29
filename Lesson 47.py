# Упражнение 47. Определение времени года.
month=str(input("Введите название месяца: "))
day=int(input("Введите номер дня: "))
if (month in ['март'] and (day>=20 and day<=31)) or (month in ['апрель'] and (day>=1 and day<=30)) \
    or (month in ['май'] and (day>=1 and day<=31)) or (month in ['июнь'] and (day>=1 and day<=20)):
    print("Весна.")
elif (month in ['июнь'] and (day>=21 and day<=30)) or (month in ['июль'] and (day>=1 and day<=31)) \
    or (month in ['август'] and (day>=1 and day<=31)) or (month in ['сентябрь'] and (day>=1 and day<=21)):
    print("Лето.")
elif (month in ['сентябрь'] and (day>=22 and day<=30)) or (month in ['октябрь'] and (day>=1 and day<=31)) \
    or (month in ['ноябрь'] and (day>=1 and day<=30)) or (month in ['декабрь'] and (day>=1 and day<=20)):
    print("Осень.")
elif (month in ['декабрь'] and (day>=21 and day<=31)) or (month in ['январь'] and (day>=1 and day<=31)) \
    or (month in ['февраль'] and (day>=1 and day<=28)) or (month in ['март'] and (day>=1 and day<=19)):
    print("Зима.")