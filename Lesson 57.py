#Счет за телефон
minute=float(input("Введите количество израсходованных минут: "))
sms=int(input("Введите количество израсходованных SMS: "))
base=15
call=0.44
nalog=0.05
if minute<=50 and sms<=50:
    print("Базовая сумма тарификации, $: ", "%.2f"%base)
    print("Сумма отчислений кол-центрам, $: ", "%.2f"%call)
    print("Налог, $: ", "%.2f"%((base+call)*nalog))
    print("Итоговая сумма к оплате, $: ", "%.2f"%((base+call)*(1+nalog)))
elif minute>50 and sms<=50:
    print("Базовая сумма тарификации, $: ", "%.2f"%base)
    print("Сумма за дополнительные минуты: ", "%.2f"%((minute-50)*0.25))
    print("Сумма отчислений кол-центрам, $: ", "%.2f"%call)
    print("Налог, $: ", "%.2f"%((base+call+(minute-50)*0.25)*nalog))
    print("Итоговая сумма к оплате, $: ", "%.2f"%((base+call+(minute-50)*0.25)*(1+nalog)))
elif minute<=50 and sms>50:
    print("Базовая сумма тарификации, $: ", "%.2f"%base)
    print("Сумма за дополнительные SMS: ", "%.2f"%((sms-50)*0.15))
    print("Сумма отчислений кол-центрам, $: ", "%.2f"%call)
    print("Налог, $: ", "%.2f"%((base+call+(sms-50)*0.15)*nalog))
    print("Итоговая сумма к оплате, $: ", "%.2f"%((base+call+(sms-50)*0.15)*(1+nalog)))
elif minute>50 and sms>50:
    print("Базовая сумма тарификации, $: ", "%.2f"%base)
    print("Сумма за дополнительные минуты: ", "%.2f"%((minute-50)*0.25))
    print("Сумма за дополнительные SMS: ", "%.2f" % ((sms - 50) * 0.15))
    print("Сумма отчислений кол-центрам, $: ", "%.2f"%call)
    print("Налог, $: ", "%.2f"%((base+call+(minute-50)*0.25+(sms - 50) * 0.15)*nalog))
    print("Итоговая сумма к оплате, $: ", "%.2f"%((base+call+(minute-50)*0.25+(sms - 50) * 0.15)*(1+nalog)))