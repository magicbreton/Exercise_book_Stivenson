#Упражнение 49. Китайский гороскоп.
year=int(input("Введите год: "))
if year%12==0:
    print("Год обезьяны.")
elif year%12==1:
    print("Год петуха.")
elif year%12==2:
    print("Год собаки.")
elif year%12==3:
    print("Год свиньи.")
elif year%12==4:
    print("Год крысы.")
elif year%12==5:
    print("Год быка.")
elif year%12==6:
    print("Год тигра.")
elif year%12==7:
    print("Год кролика.")
elif year%12==8:
    print("Год дракона.")
elif year%12==9:
    print("Год змеи.")
elif year%12==10:
    print("Год лошади.")
elif year%12==11:
    print("Год козы.")