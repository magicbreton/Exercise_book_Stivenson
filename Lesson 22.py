a=float(input("Длина первой стороны: "))
b=float(input("Длина второй стороны: "))
c=float(input("Длина третьей стороны: "))
p=(a+b+c)/2
print("Площадь треугольника: ", (p*(p-a)*(p-b)*(p-c))**0.5)