note=str(input("Введите обозначение ноты: "))
new_note=list(note)
if new_note[0] in ['C','c']:
    print("Частота: ", 261.63/(2**(4-int(new_note[1]))))
elif new_note[0] in ['D','d']:
    print("Частота: ", 293.66/(2**(4-int(new_note[1]))))
elif new_note[0] in ['E','e']:
    print("Частота: ", 329.63/(2**(4-int(new_note[1]))))
elif new_note[0] in ['F','f']:
    print("Частота: ", 349.23/(2**(4-int(new_note[1]))))
elif new_note[0] in ['G','g']:
    print("Частота: ", 392.00/(2**(4-int(new_note[1]))))
elif new_note[0] in ['A','a']:
    print("Частота: ", 440.00/(2**(4-int(new_note[1]))))
elif new_note[0] in ['B','b']:
    print("Частота: ", 493.88/(2**(4-int(new_note[1]))))
