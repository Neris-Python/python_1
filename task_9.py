ip = input("Введите IP-адрес: ")
parts = ip.split('.')
if len(parts) != 4:
    print("Не корректный IP!")
else:
    point= True
    for part in parts:
        if not part.isdigit():
            point = False
            break
        num = int(part)
        if num < 0 or num > 255:
            point = False
            break

    if point:
        print("Корректный IP-адрес!")
    else:
        print("Не корректный IP!")
