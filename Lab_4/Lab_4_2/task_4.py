import numpy as np
a, b, n = -3, 5, 1000
x = np.linspace(a, b, n+1)
y = x**5+3*x**4+6*x**2+1
h = (b - a) / n
integral1 = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
print(f"Определенный интеграл: {integral1:.4f}")

a, b, c, d, n_points = -2, 4, -1, 1, 100000
x_rand = np.random.uniform(a, b, n_points)
y_rand = np.random.uniform(c, d, n_points)
f_values = x_rand**5 + 3*x_rand**4*y_rand + 6*x_rand**2*y_rand**2 + 1
area = (b - a) * (d - c)
integral2 = area * np.mean(f_values)
print(f"Двойной интеграл: {integral2:.4f}")
