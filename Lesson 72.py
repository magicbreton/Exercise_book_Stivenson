#Упражнение 72. Игра Fizz-Buzz

#Генерируем список из ста элементов (от 1 до 100) для проверки его в последующем
answer = [x for x in range(1, 101)]
#print(answer)
#Создаем пустой список
answer_mask = []
for x in answer:
    if x % 3 == 0 and x % 5 == 0:
        answer_mask.append("Fizz-Buzz")
    elif x % 3 == 0:
        answer_mask.append("Fizz")
    elif x % 5 == 0:
        answer_mask.append("Buzz")
    else:
        answer_mask.append(x)
#print(answer_mask)
print(*answer_mask, sep='\n')