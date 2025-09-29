import time

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            name = func.__name__
            args_str = ""
            for a in args:
                if args_str != "":
                    args_str += ", "
                args_str += str(a)

            kwargs_str = ""
            for k in kwargs:
                if kwargs_str != "":
                    kwargs_str += ", "
                kwargs_str += str(k) + "=" + str(kwargs[k])

            all_args = args_str
            if kwargs_str:
                if all_args:
                    all_args += ", " + kwargs_str
                else:
                    all_args = kwargs_str
            with open(filename, "a") as f:
                f.write(f"{t} - {name}({all_args})\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("log.txt")
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
print("Уникальные элементы:", result)
