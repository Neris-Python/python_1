word_1 = input("Первое слово: ").lower()
word_2 = input("Второе слово: ").lower()

sorted1 = list(word_1)
sorted1.sort()

sorted2 = list(word_2)
sorted2.sort()

if sorted1 == sorted2:
    print("True")
else:
    print("False")
