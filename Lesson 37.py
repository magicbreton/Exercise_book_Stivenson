letter=str(input("Введите букву латинского алфавита: "))
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("Введена гласная буква.")
elif letter in ['y']:
    print("Введенная буква может быть как гласной, так и согласной.")
else:
    print("Введена согласная буква.")