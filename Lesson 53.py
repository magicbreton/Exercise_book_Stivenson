# Упражнение 53. Числовые оценки - в буквенные.
num=float(input("Введите числовую оценку: "))
if num>=4.0:
    print("Буквенный номинал оценки: А+")
elif num>=3.85 and num<4.0:
    print("Буквенный номинал оценки: А")
elif num>=3.5 and num<3.85:
    print("Буквенный номинал оценки: А-")
elif num>=3.15 and num<3.5:
    print("Буквенный номинал оценки: B+")
elif num>=2.85 and num<3.15:
    print("Буквенный номинал оценки: B")
elif num>=2.5 and num<2.85:
    print("Буквенный номинал оценки: B-")
elif num>=2.15 and num<2.5:
    print("Буквенный номинал оценки: C+")
elif num>=1.85 and num<2.15:
    print("Буквенный номинал оценки: C")
elif num>=1.5 and num<1.85:
    print("Буквенный номинал оценки: C-")
elif num>=1.15 and num<1.5:
    print("Буквенный номинал оценки: D+")
elif num>=0.5 and num<1.15:
    print("Буквенный номинал оценки: D")
elif num>=0 and num<0.5:
    print("Буквенный номинал оценки: F")