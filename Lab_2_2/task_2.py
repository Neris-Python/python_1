def merge_dicts(d1, d2):
    for key in d2:
        if key in d1:
            if type(d1[key]) == dict and type(d2[key]) == dict:
                merge_dicts(d1[key], d2[key])
            else:
                d1[key] = d2[key]
        else:
            d1[key] = d2[key]
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
print("Первый словарь:", dict_a)
print("Второй словарь:", dict_b)
merge_dicts(dict_a, dict_b)
print("Объединённый словарь:", dict_a)
