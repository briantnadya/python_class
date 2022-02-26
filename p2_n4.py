import numpy as np
from scipy.linalg import lu

A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = lu(A)
print(np.allclose(A - P @ L @ U, np.zeros((3, 3))))

print(P)
print(L)
print(U)

P = np.linalg.inv(P)

# to check the results let's multiply and subtract the results:
print(np.dot(P, A) - np.dot(L, U))
