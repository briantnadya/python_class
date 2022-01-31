import numpy as np
import matplotlib.pyplot as plt


def func(k, x_arg):
    return np.cos(k * x_arg)


x = np.linspace(0, 10, 50)
k_param = [1, 5]
y1 = []
y2 = []


for i in x:
    y1.append(func(i, k_param[0]))
    y2.append(func(i, k_param[1]))

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
