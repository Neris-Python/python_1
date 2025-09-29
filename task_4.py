lst_1 = input("Первый набор чисел: ").split()
for i in range(len(lst_1)):
    lst_1[i] = int(lst_1[i])
lst_2 = input("Второй набор чисел: ").split()
for i in range(len(lst_2)):
    lst_2[i] = int(lst_2[i])

common = []
for num in lst_1:
    if num in lst_2 and num not in common:
        common.append(num)
print("1. Числа в обоих наборах:", common)

only1 = []
for num in lst_1:
    if num not in lst_2:
        only1.append(num)
print("   Только в первом:", only1)

only2 = []
for num in lst_2:
    if num not in lst_1:
        only2.append(num)
print("   Только во втором:", only2)

unique = only1 + only2
print("3. Числа из обоих, кроме общих:", unique)
