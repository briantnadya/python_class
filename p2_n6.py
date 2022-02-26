import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([2, 5, 11])

X_pseudo = np.linalg.lstsq(A, b, rcond=None)
print(X_pseudo)

# to check the correctness of the pseudo solution let's find the dot product:
print(np.dot(A, X_pseudo[0]))


# we can also check the residual by creating the function below and printing the result below it:
def Q(A, b, x_p):
    return (np.linalg.norm(np.dot(A, x_p) - b)) ** 2


print("Residual equals: {}".format(Q(A, b, X_pseudo[0])))