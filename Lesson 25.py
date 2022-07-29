s=int(input("Введите количество секунд: "))
day=s//86400
hour=s%86400//3600
minute=s%86400%3600//60
second=s%86400%3600%60
print("Длительность: ", day, ":", "%02d"%hour, ":", "%02d"%minute, ":", "%02d"%second)