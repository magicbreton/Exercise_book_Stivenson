# Упражнение 51. Корни квадратичной функции.
a=float(input("Введите значение коэффициента a: "))
b=float(input("Введите значение коэффициента b: "))
c=float(input("Введите значение коэффициента c: "))
if (b**2 - 4*a*c)<0:
    print("Квадратное уравнение не имеет действительных корней.")
elif (b**2 - 4*a*c)==0:
    print("Квадратное уравнение имеет два одинаковых действительных корня: ", (-b/(2*a)))
elif (b**2 - 4*a*c)>0:
    print("Квадратное уравнение имеет два разных действительных корня: ", \
          ((-b+(b**2-4*a*c)**0.5)/(2*a)), \
          ((-b-(b**2-4*a*c)**0.5)/(2*a)))