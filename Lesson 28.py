weight=float(input("Масса тела в килограммах: "))
height=float(input("Рост в сантиметрах: "))
print("Индекс массы тела (MBI): ", "%.6f"%(weight/(height**2)))