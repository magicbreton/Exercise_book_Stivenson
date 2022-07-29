day=int(input("Введите дату: "))
month=str(input("Введите месяц: "))
new_month1=['Январь', 'январь']
new_month2=['Июль', 'июль']
new_month3=['Декабрь', 'декабрь']
if day==1 and month in new_month1:
    print("Новый год.")
elif day==1 and month in new_month2:
    print("День Канады.")
elif day==25 and month in new_month3:
    print("Рождество.")
else:
    print("На заданную дату праздники не приходятся.")