import re
string = input("Введите строку: ")
words = re.split(r'[,.\n?! ]+', string)
word_count = {}
for word in words:
    lower_word = word.lower()
    if lower_word in word_count:
        word_count[lower_word] += 1
    else:
        word_count[lower_word] = 1
print("Словарь {слово: количество}:")
for word, count in word_count.items():
    print(word, count)
unique_count = len(word_count)
print("Количество уникальных слов:", unique_count)