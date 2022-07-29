#Упражнение 74. Квадратный корень

x = float(input("Введите число: "))

guess = x/2
while abs(guess*guess-x) >= 10**(-12):
    guess = (guess+x/guess)/2
print("Квадратный корень из х равен: ", guess)