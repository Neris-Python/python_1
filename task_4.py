amount = int(input("Введите сумму в рублях: "))
bills_100 = amount // 100
amount %= 100
bills_50 = amount // 50
amount %= 50
bills_10 = amount // 10
amount %= 10
bills_5 = amount // 5
amount %= 5
coins_2 = amount // 2
amount %= 2
coins_1 = amount
print("100 руб:", bills_100)
print("50 руб:", bills_50)
print("10 руб:", bills_10)
print("5 руб:", bills_5)
print("2 руб:", coins_2)
print("1 руб:", coins_1)
