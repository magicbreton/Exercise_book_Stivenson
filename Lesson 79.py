#Упражнение 79. Наибольший общий делитель.

n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
d_0 = []
d_0.append(n)
d_0.append(m)
d = min(d_0)
print(d)
for d in range(d, 1, -1):
    if n%d!=0 and m%d!=0:
        d-=1
    elif n%d==0 and m%d==0:
        print("Наибольший общий делитель: ", d)