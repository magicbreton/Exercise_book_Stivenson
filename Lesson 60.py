# Упражнение 60. На какой день недели выпадает 1 января?
from math import floor
year=int(input("Введите год: "))
day=(year + floor((year-1)/4) - floor((year-1)/100) + floor((year-1)/400))%7
if day==0:
    print("Воскресенье.")
elif day==1:
    print("Понедельник.")
elif day==2:
    print("Вторник.")
elif day==3:
    print("Среда.")
elif day==4:
    print("Четверг.")
elif day==5:
    print("Пятница.")
elif day==6:
    print("Суббота.")