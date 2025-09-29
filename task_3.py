lst = input("Введите числа: ").split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
unique_lst = []
for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)
unique_lst.sort()
print(unique_lst[len(unique_lst)-2])
