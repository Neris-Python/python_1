lst = input("Введите числа через пробел: ")
numbers_lst = lst.split()
numbers = []
for num_lst in numbers_lst:
    numbers.append(float(num_lst))
unique = []
seen = {}
for num in numbers:
    if num not in seen:
        unique.append(num)
        seen[num] = 1
    else:
        seen[num] += 1
print("1. Уникальные числа:", unique)
repeating = []
for num, count in seen.items():
    if count > 1:
        repeating.append(num)
print("2. Повторяющиеся числа:", repeating)
even = []
odd = []
for num in numbers:
    if num == int(num):
        if int(num) % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
print("3. Чётные:", even)
print("   Нечётные:", odd)
negative = [num for num in numbers if num < 0]
print("4. Отрицательные:", negative)
floats = [num for num in numbers if num != int(num)]
print("5. Числа с плавающей точкой:", floats)
sum_multiples_5 = 0
for num in numbers:
    if num % 5 == 0:
        sum_multiples_5 += num
print("6. Сумма чисел, кратных 5:", sum_multiples_5)
if numbers:
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print("7. Самое большое:", max_num)
    print("8. Самое маленькое:", min_num)
else:
    print("Список пустой!")
