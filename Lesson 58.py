# Упражнение 58. Високосный год?
year = int(input("Введите год: "))
if year % 400 == 0:
    print("Високосный год.")
elif year % 400 != 0 and year % 100 == 0:
    print("Невисокосный год.")
elif year % 400 != 0 and year % 100 == 0 and year % 4 == 0:
    print("Високосный год.")
else:
    print("Високосный год.")