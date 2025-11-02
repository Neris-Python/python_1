seconds = int(input("Введите количество секунд: "))
minute = seconds // 60
remainder = seconds % 60
if minute % 10 == 1 and minute % 100 != 11:
    min_text = "минута"
elif 2 <= minute % 10 <= 4 and not (12 <= minute % 100 <= 14):
    min_text = "минуты"
else:
    min_text = "минут"
if remainder % 10 == 1 and remainder % 100 != 11:
    sek_text = "секунда"
elif 2 <= remainder % 10 <= 4 and not (12 <= remainder % 100 <= 14):
    sek_text = "секунды"
else:
    sek_text = "секунд"
print(minute, min_text, remainder, sek_text)