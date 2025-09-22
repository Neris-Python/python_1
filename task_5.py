num = int(input("Введите число: "))
if num % 7 == 0:
    print("Магическое число!")
else:
    s = str(num)
    summa = 0
    for c in s:
        summa += int(c)
    print("Сумма цифр:", summa)
