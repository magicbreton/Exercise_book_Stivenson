#Упражнение 77. Таблица умножения.

names_colones = [x for x in range(1, 11)]
print('\t','{:}{:6}{:6}{:6}{:6}{:6}{:6}{:6}{:6}{:6}'.format(*names_colones))
names_rows = [y for y in range(1, 11)]
for z in names_rows:
    r = map(lambda x: x*z, names_colones)
    print(z,'\t', '{:}{:6}{:6}{:6}{:6}{:6}{:6}{:6}{:6}{:6}'.format(* r))