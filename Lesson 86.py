#Упражнение 86. Плата за такси.

# @param s - расстояние поездки, км.
# return summa - итоговая сумма оплаты такси.

def priceTaxi(s):
    mainPart = 4
    floatingRate = 0.25
    if s >= 0:
        summa = mainPart + floatingRate*(s*1000/140)
        print('Итоговая сумма оплаты в такси: ', "%.2f" % summa, '$.')
    elif s < 0:
        print('Ошибка. Расстояние не может быть выражено отрицательным числом.')

priceTaxi(6.67)