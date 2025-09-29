lst = input("Введите элементы списка через пробел: ")
items = lst.split()
unique_list = []
for item in items:
    is_duplicate = False
    for u in unique_list:
        if u == item:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_list.append(item)
print("Список без дубликатов:", unique_list)
