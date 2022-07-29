#Упражнение 75. Палиндром или нет?

word = input("Введите слово: ")
word_list = list(word) #разбиваем на список отдельных элементов
if len(word_list) % 2 == 0:
    word_list_1 = word_list[0:int(len(word_list)/2)]
    word_list_2 = word_list[-1:-int((len(word_list)/2+1)):-1]
    if word_list_1 == word_list_2:
        print("Введенное слово - палиндром.")
    else:
        print("Введенное слово - не палиндром.")
else:
    word_list_1 = word_list[0:int(len(word_list)//2)]
    word_list_2 = word_list[-1:-int((len(word_list)//2+1)):-1]
    if word_list_1 == word_list_2:
        print("Введенное слово - палиндром.")
    else:
        print("Введенное слово - не палиндром.")