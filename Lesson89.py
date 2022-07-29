#Упражнение 89. Переводим целые числа в числительные.
def Int_To_Numeral(init):
    a_0 = [x for x in range(1, 13, 1)]
    numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',\
            'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    if init in a_0:
        numeral = numbers[init-1]
    else:
        numeral = ('')
    return numeral

if __name__ == "__main__":
    Int_To_Numeral(init='')



