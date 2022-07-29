#Упражнение 70. Биты четности

bits = input("Введите восемь бит: ")
while bits != "":
    if len(bits) != 8:
        print("Количество введенных символов должно равняться 8.")
    elif bits[0] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    elif bits[1] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    elif bits[2] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    elif bits[3] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    elif bits[4] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    elif bits[5] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    elif bits[6] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    elif bits[7] not in ['0', '1']:
        print("Должны быть введены только 0 и 1.")
    else:
        bits_int = [int(x) for x in bits]
        if sum(bits_int) % 2 == 0:
            print("Бит четности равен 0.")
        elif sum(bits_int) % 2 == 1:
            print("Бит четности равен 1.")
    bits = input("Введите восемь бит: ")


