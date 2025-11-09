import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.exp(np.cos(x))+np.log(np.cos(0.6*x)**2+1)*np.sin(x)
plt.plot(x, y, label="График", color="blue")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции f(x)=e^cos(x) + ln(cos^2(0.6x) + 1) * sin(x)")
plt.legend()
plt.savefig("task1_1.png")
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = -np.log((np.cos(x)+np.sin(x))**2+2.5)+10
plt.plot(x, y, label="График", color="blue")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.title("График функции h(x)=-ln((cos(x)+sin(x))^2+2.5)+10")
plt.legend()
plt.savefig("task1_2.png")
