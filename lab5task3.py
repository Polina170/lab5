print("Для завершения работы программы напишите 'stop' " )
word = input("Введите слово:")
while word != "stop":
    if 'ф' in word.lower():
        print("Это редкое слово!")
    else:
        print("Это не редкое слово")
    word = input("Введите слово:")