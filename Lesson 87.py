#Упражнение 87. Расчет стоимости доставки.

# @param n - количество товаров

def summaDelivery(n):
    if n > 1:
        summa = 10.95 + 2.95
        print('Итоговая сумма доставки: ', "%.2f" % summa, '$.')
    elif n == 1:
        summa = 10.95
        print('Итоговая сумма доставки: ', "%.2f" % summa, '$.')
    elif n < 0:
        print('Ошибка. Количество товаров не может быть выражено отрицательным числом.')
n = int(input('Количество товаров в заказе: '))
summaDelivery(n)