sum=int(input("Сумма сдачи в центах: "))
print("Количество двухдолларовых монет: ", sum//200) #***количество целых двухдолларовых монет***
print("Количестов однодолларовых монет: ", (sum%200)//100) #количество однодолларовых монет
print("Количество двадцатипятицентовых монет: ", (sum%100)//25) #количество двадцатицентовых монет
print("Количество десятицентовых монет: ", (sum%25)//10) #количество десятицентовых монет
print("Количество пятицентовых монет: ", (sum%25%10)//5) #количество пятицентовых монет
print("Количество одноцентовых монет: ", (sum%5)//1) #количество одноцентовых монет

