# Упражнение 62. Играем в рулетку.
import random

bid=str(input("Сделайте вашу ставку: "))
all=['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31', '33', '35',\
     '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36',
     '0', '00']

r=random.choice(all)
red=['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
black=['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']
zero=['0']
zeroo=['00']
even=['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31', '33', '35']
odd=['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36']
r1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
r2=['19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
print("Выпавший номер: ", r)
print("Выигрывшая ставка: ", r)
if r in red:
    print("Выигравшая ставка: красное")
    if r in even:
        print("Выигравшая ставка: нечетное")
        if r in r1:
            print("Выигравшая ставка: от 1 до 18")
        elif r in r2:
            print("Выигравшая ставка: от 19 до 36")
    elif r in odd:
        print("Выигравшая ставка: четное")
        if r in r1:
            print("Выигравшая ставка: от 1 до 18")
        elif r in r2:
            print("Выигравшая ставка: от 19 до 36")
elif r in black:
    print("Выигравшая ставка: черное")
    if r in even:
        print("Выигравшая ставка: нечетное")
        if r in r1:
            print("Выигравшая ставка: от 1 до 18")
        elif r in r2:
            print("Выигравшая ставка: от 19 до 36")
    elif r in odd:
        print("Выигравшая ставка: четное")
        if r in r1:
            print("Выигравшая ставка: от 1 до 18")
        elif r in r2:
            print("Выигравшая ставка: от 19 до 36")