import math

s=float(input("Длина стороны правильного многоугольника: "))
n=float(input("Количество сторон правильного многоугольника: "))
d=(n*s**2)/(4*math.tan(math.pi/n))
print("Площадь правильного многоугольника: ", "%.2f"%d)