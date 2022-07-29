# Упражнение 61. Действительный номерной знак машины?
num=str(input("Введите номер машины: "))
new_num=list(num)
alf=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',\
     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
book=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
if len(new_num)==6 and new_num[0] in alf and new_num[1] in alf and new_num[2] in alf and new_num[3] in book \
    and new_num[4] in book and new_num[5] in book:
    print("Старый формат.")
elif len(new_num)==7 and new_num[0] in book and new_num[1] in book and new_num[2] in book and new_num[3] in book \
    and new_num[4] in alf and new_num[5] in alf and new_num[6] in alf:
    print("Новый формат.")
else:
    print("Неверный формат.")
