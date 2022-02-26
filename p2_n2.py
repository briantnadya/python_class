import numpy as np

A = np.array([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0, -5], [11, 4, -7]])
b = np.array([1, 7, 12, 7, 15])
X_pseudo = np.linalg.lstsq(A, b, rcond=None)
print("Pseudo solution is {}".format(X_pseudo))

# to check the correctness of the pseudo solution let's find the dot product:
print("This result should be close to b vector: {}".format(np.dot(A, X_pseudo[0])))


# we can also check the residual by creating the function below and printing the result below it:
def Q(A, b, x_p):
    return (np.linalg.norm(np.dot(A, x_p) - b)) ** 2


print(Q(A, b, X_pseudo[0]))


