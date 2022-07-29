#Упражнение 83. Максимальное число в последовательности.

import random
import copy

number = [x for x in range(1, 101)]
sub = []
maximum = []
index = []
while len(sub) != 100:
    sub.append(random.choice(number))
    maximum.append(max(sub))

for i in range(len(maximum)-1):
    if maximum[i] < maximum[i+1]:
        index.append(maximum.index(maximum[i+1]))

sub_copy = copy.copy(sub)

for y in index:
    sub[y] = str(sub[y]) +'<== Обновление'
print("\n".join(map(str, sub)))
print('Максимальное значение в ряду: ', max(sub_copy))
print('Количество смен максимального значения: ', len(index))