import random
number = random.randint(1, 100)
while True:
    guess = int(input("Введите вашу догадку (1-100): "))
    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print("Поздравляем! Вы угадали число.")
        break
