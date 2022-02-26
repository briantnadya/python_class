import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D


def Q(x, y, z):
    return x ** 2 + y ** 2 + z ** 2


fig = figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
X = np.arange(-15, 15, 1)
Y = np.arange(-15, 15, 1)
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Q(X, 10*X-14, 29-21*X))
#ax.plot_surface(X, Y, Q(X, Y, 6 - 4 * X + 2.5 * Y))
show()

A = np.array([[1, 2, -1], [8, -5, 2]])
b = np.array([1, 12])
print(np.linalg.lstsq(A, b, rcond=None))
