def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            if len(args) != len(types):
                raise TypeError("Количество аргументов не совпадает с количеством типов")
            i = 0
            while i < len(args):
                if type(args[i]) != types[i]:
                    raise TypeError("Аргумент", i+1, "должен быть типа", types[i].__name__+ ", а получен", type(args[i]).__name__)
                i += 1
            return func(*args)
        return wrapper
    return decorator

@type_check(list)
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
n = 0
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
print("Исходный список:", list_a)
result = unique_elements(list_a)
print("Результат unique_elements:", result)