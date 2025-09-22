base_minutes = 60
base_sms = 30
base_internet_mb = 1024
base_price = 24.99

extra_minute_price = 0.89
extra_sms_price = 0.59
extra_mb_price = 0.79

minutes_used = int(input("Введите количество использованных минут: "))
sms_used = int(input("Введите количество использованных SMS: "))
internet_used_mb = int(input("Введите использованный интернет (в МБ): "))

extra_minutes = max(0, minutes_used - base_minutes)
extra_sms = max(0, sms_used - base_sms)
extra_mb = max(0, internet_used_mb - base_internet_mb)

extra_minutes_cost = round(extra_minutes * extra_minute_price,2)
extra_sms_cost = round(extra_sms * extra_sms_price,2)
extra_mb_cost = round(extra_mb * extra_mb_price,2)

subtotal = base_price + extra_minutes_cost + extra_sms_cost + extra_mb_cost
tax = subtotal * 0.02
total = subtotal + round(tax,2)

print("Базовая сумма тарификации:", base_price, "руб.")

if extra_minutes > 0:
    print("Дополнительные минуты:", extra_minutes, "шт., стоимость:", extra_minutes_cost, "руб.")
if extra_sms > 0:
    print("Дополнительные SMS:", extra_sms, "шт., стоимость:", extra_sms_cost, "руб.")
if extra_mb > 0:
    print("Дополнительный интернет:", extra_mb, "МБ, стоимость:", extra_mb_cost, "руб.")

print("Налог (2%):", round(tax,2), "руб.")
print("Итоговая сумма к оплате:", total, "руб.")
