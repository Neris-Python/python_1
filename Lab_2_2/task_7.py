def merge_sorted_list(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
print("Первый отсортированный список:", l1)
print("Второй отсортированный список:", l2)
merged = merge_sorted_list(l1, l2)
print("Объединённый отсортированный список:", merged)
