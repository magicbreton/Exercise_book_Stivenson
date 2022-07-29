#Упражнение 90. Двенадцать дней Рождества.

from Lesson89 import Int_To_Numeral

def main(init):
    couplet = ['Twelve drummers drumming,\n', 'Eleven pipers piping,\n', 'Ten lords a-leaping,\n'
               , 'Nine ladies dancing,\n', 'Eight maids a-milking,\n', 'Seven swans a-swimming,\n'
                , 'Six geese a-laying,\n', 'Five golden rings,\n', 'Four calling birds,\n'
                , 'Three French hens,\n', 'Two turtle doves,\n', 'And a partridge in a pear tree.\n']
    print('On the ', Int_To_Numeral(init), ' day of Christmas\n'
            'my true love sent to me:')
    if init == 1:
        print('A partridge in a pear tree.\n')
    elif init == 2:
        print(''.join(couplet[10:12]))
    elif init == 3:
        print(''.join(couplet[9:12]))
    elif init == 4:
        print(''.join(couplet[8:12]))
    elif init == 5:
        print(''.join(couplet[7:12]))
    elif init == 6:
        print(''.join(couplet[6:12]))
    elif init == 7:
        print(''.join(couplet[5:12]))
    elif init == 8:
        print(''.join(couplet[4:12]))
    elif init == 9:
        print(''.join(couplet[3:12]))
    elif init == 10:
        print(''.join(couplet[2:12]))
    elif init == 11:
        print(''.join(couplet[1:12]))
    elif init == 12:
        print(''.join(couplet))
main(1)
main(2)
main(3)
main(4)
main(5)
main(6)
main(7)
main(8)
main(9)
main(10)
main(11)
main(12)
print('And a partridge in a pear tree.')
