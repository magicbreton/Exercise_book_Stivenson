import math

t1=float(input("Широта точки 1: "))
g1=float(input("Долгота точки 1: "))
t2=float(input("Широта точки 2: "))
g2=float(input("Долгота точки 2: "))
distance=6371.01*math.acos(math.sin(math.radians(t1))*math.sin(math.radians(t2))+math.cos(math.radians(t1))*math.cos(math.radians(t2))*math.cos(math.radians(g1-g2)))
print("Расстояние между двумя точками: ", distance, "км")