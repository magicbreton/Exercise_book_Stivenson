#Упражнение 68. Средняя оценка.
letters=[]#формируем пустой список
letter=str(input("Введите буквенную оценку: "))
while letter !="":
    if letter in ['A+']:
        letters.append(4.0)
    elif letter in ['A']:
        letters.append(4.0)
    elif letter in ['A-']:
        letters.append(3.7)
    elif letter in ['B+']:
        letters.append(3.3)
    elif letter in ['B']:
        letters.append(3.0)
    elif letter in ['B-']:
        letters.append(2.7)
    elif letter in ['C+']:
        letters.append(2.3)
    elif letter in ['C']:
        letters.append(2.0)
    elif letter in ['C-']:
        letters.append(1.7)
    elif letter in ['D+']:
        letters.append(1.3)
    elif letter in ['D']:
        letters.append(1.0)
    elif letter in ['F']:
        letters.append(0.0)
    letter=str(input("Введите буквенную оценку: "))
    if letter =="":
        break
print("Средняя оценка: ", sum(letters)/len(letters))
