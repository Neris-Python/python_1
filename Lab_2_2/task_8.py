import time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        print("Время выполнения функции", func.__name__, elapsed_ms,  "мс")
        return result
    return wrapper

@timing
def unique_elements(lst):
    unique = []
    def helper(sublist):
        i = 0
        while i < len(sublist):
            item = sublist[i]
            if type(item) == list:
                helper(item)
            else:
                found = False
                for u in unique:
                    if u == item:
                        found = True
                        break
                if not found:
                    unique.append(item)
            i += 1
    helper(lst)
    return unique

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
print("Исходный список:", list_a)
result = unique_elements(list_a)
print("Результат unique_elements:", result)
