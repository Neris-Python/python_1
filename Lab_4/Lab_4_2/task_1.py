import numpy as np
print("Введите массив arr: ")
arr = input(np.array)
winter_sum=arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]
summer_sum=arr[6]+arr[7]+arr[8]+arr[9]+arr[10]+arr[11]
if winter_sum>summer_sum:
    print("Траты на транспорт в зимний период выше, чем в летний")
elif summer_sum>winter_sum:
    print("Траты на транспорт в летний период выше, чем в зимний")
else:
    print("Траты в зимний и летний период одинаковые")
first_half_array = arr[:6]
first_max_index = np.argmax(first_half_array)
print(f"{first_max_index + 1} номер месяца в зимнем периоде, в котором траты наибольшие")
second_half_array = arr[6:]
second_max_index = np.argmax(second_half_array)
print(f"{second_max_index + 7} номер месяца в летнем периоде, в котором траты наибольшие")