def flatten_list(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            inner = lst[i]
            lst.pop(i)
            j = 0
            while j < len(inner):
                lst.insert(i + j, inner[j])
                j += 1
        else:
            i += 1
    has_list = False
    for item in lst:
        if type(item) == list:
            has_list = True
            break
    if has_list:
        flatten_list(lst)


list_a = [2, 4, 1, [42], 5, [8, [1, [], 10, [3]]]]
print("Исходный список:", list_a)
flatten_list(list_a)
print("Плоский список:", list_a)
