import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x1 = np.linspace(-10, 2.9, 100)
x2 = np.linspace(3.1, 10, 100)
y1 = 5 / (x1**2 - 9)
y2 = 5 / (x2**2 - 9)
plt.plot(x1, y1, label="График", color="blue")
plt.plot(x2, y2, color="blue")
plt.axvline(x=3, color='red', linestyle='--', label="Асимптота x=3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции f(x)=5/(x^2-9)")
plt.legend()
plt.savefig("task2.png")
