words = []
print("Для завершения работы программы напишите 'stop' " )
word = input("Введите слово:")
while word != "stop":
    words.append(word)
    word = input("Введите слово:")
res = " ".join(words)
print(res)