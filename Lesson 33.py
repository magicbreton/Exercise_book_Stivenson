a=int(input("Введите первое целое число: "))
b=int(input("Введите второе целое число: "))
c=int(input("Введите третье целое число: "))
x=[a,b,c]
minx=min(x)
maxx=max(x)
print(int(minx), (a+b+c-int(minx)-int(maxx)),int(maxx))