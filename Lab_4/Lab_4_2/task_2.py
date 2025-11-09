import numpy as np
print("Длины участков: ")
section_lengths = np.fromstring(input(), sep=' ')
print("Скорости на участках: ")
section_speeds = np.fromstring(input(), sep=' ')
k = int(input("Номер участка k, на котором автомобиль въехал на дорогу: ")) - 1
p = int(input("Номер участка p, после которого автомобиль выехал: "))
length = np.sum(section_lengths[k:p])
print(f"Длина дороги S= {length:.2f} км")
speed = np.sum(section_speeds[k:p]) / (p-k)
print(f"Средняя скорость на участках V= {speed:.2f} км/ч")
time = np.sum(section_lengths[k:p] / section_speeds[k:p])
print(f"Время в пути T= {time:.2f} ч")
