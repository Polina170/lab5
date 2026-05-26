total = int(input('Введите количество слов: '))
words = []
for i in range(total):
    word = input("ведите слово: ")
    words.append(word)
res = " ".join(words)
print(res)