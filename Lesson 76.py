#Упражнение 76. Многословные палиндромы.

word = input("Введите фразу: ")
word_list = list(word) #разбиваем на список отдельных элементов
word_list_0 = []
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for x in word_list:
    if x in abc:
        word_list_0.append(x)
    elif x in ABC:
        word_list_0.append(abc[ABC.index(x)])

if len(word_list_0) % 2 == 0:
    word_list_1 = word_list_0[0:int(len(word_list_0)/2)]
    word_list_2 = word_list_0[-1:-int((len(word_list_0)/2+1)):-1]
    if word_list_1 == word_list_2:
        print("Введенная фраза - палиндром.")
    else:
        print("Введенная фраза - не палиндром.")
else:
    word_list_1 = word_list_0[0:int(len(word_list_0)//2)]
    word_list_2 = word_list_0[-1:-int((len(word_list_0)//2+1)):-1]
    if word_list_1 == word_list_2:
        print("Введенная фраза - палиндром.")
    else:
        print("Введенная фраза - не палиндром.")