nums = [(3,6,9),(7,8,15),(8,3,11),(3,9,12),(2,4,6),(1,9,10),(7,2,9),(5,7,12)]
errors = 0
good = 0
for a, b, correct in nums:
    if errors == 3:
        print("Вы сделали 3 ошибки.")
        break
    answer = input(f"{a} + {b} = ")
    if int(answer) == correct:
        print("Правильно!")
        good += 1
    else:
        print('Ошибка! Ответ неверный!')
        errors += 1
print("Игра окончена, правильных ответов:", good)