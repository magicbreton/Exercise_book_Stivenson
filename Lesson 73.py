#Упражнение 73. Код Цезаря

phrase = input("Введите фразу: ")
shift = input("Введите значение сдвига: ")
phrase_mask = []

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

phrase_list = list(phrase)

for x in phrase:
    if x in abc:
        phrase_mask.append(abc[abc.index(x)+int(shift)])
    elif x in ABC:
        phrase_mask.append(ABC[ABC.index(x) + int(shift)])
    else:
        phrase_mask.append(x)

print("Фраза после шифрования: ", "".join(phrase_mask))


