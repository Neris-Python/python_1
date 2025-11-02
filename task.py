# Если длина строки кратна 5 и содержит только буквы, заменить а (А) на 0
# Если длина строки кратна 3 и состоит только из чисел, заменить нечётные числа на 0
# Иначе вывести строку в обратном порядке
string = input("Введите строку: ")
if len(string) % 5 == 0 and string.isalpha():
    new_string = string.replace('a', '0').replace('A', '0')
    print(new_string)
elif len(string) % 3 == 0 and string.isdigit():
    new_string = string.replace('1', '0').replace('3', '0').replace('5', '0').replace('7', '0').replace('9', '0')
    print(new_string)
else:
    print(string[::-1])