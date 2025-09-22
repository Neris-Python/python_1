string = input("Введите строку: ")
vowels = 'aeiouAEIOU'
result = ''
for letter in string:
    if letter not in vowels:
        result += letter
print("Строка без гласных:", result)
