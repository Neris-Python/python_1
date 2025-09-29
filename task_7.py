string = input("Введите строку: ")
result = ""
i = 0
while i < len(string):
    current_char = string[i]
    count = 0
    while i < len(string) and string[i] == current_char:
        count += 1
        i += 1
    result += current_char + str(count)
print(result)
