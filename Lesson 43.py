noise=float(input("Введите частоту звука: "))
if noise>260.63 and noise<262.63:
    print("Нота С4.")
elif noise>292.66 and noise<294.66:
    print("Нота D4.")
elif noise>328.63 and noise<330.63:
    print("Нота Е4.")
elif noise>348.23 and noise<350.23:
    print("Нота F4.")
elif noise>391 and noise<393:
    print("Нота G4.")
elif noise>439 and noise<441:
    print("Нота А4.")
elif noise>492.88 and noise<494.88:
    print("Нота В4.")
else:
    print("Частота за пределами диапазона.")