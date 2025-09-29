ip = input("Введите IP-адрес: ")
parts = ip.split('.')

if len(parts) != 4:
    print("Не корректный IP!")
else:
    p1, p2, p3, p4 = parts
    if (p1.isdigit() and p2.isdigit() and p3.isdigit() and p4.isdigit()):
        n1, n2, n3, n4 = int(p1), int(p2), int(p3), int(p4)
        if 0 <= n1 <= 255 and 0 <= n2 <= 255 and 0 <= n3 <= 255 and 0 <= n4 <= 255:
            print("Корректный IP-адрес!")
        else:
            print("Не корректный IP!")
    else:
        print("Не корректный IP!")
