import numpy as np
import math as math


def bin_distr(n, k, p, q):
    prob = (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * math.pow(p, k) * math.pow(q, n - k)
    return prob


n_trials = 4
n_successes = 2
p = 0.5
q = 1.0 - p
k, n = 0, 100000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d

for i in range(0, n):
    if x[i] == 2:
        k = k + 1

print(k, n, float(k) / n)
# we can see how with increasing the number n the numerical probability is getting closer to the theoretical one
print("The theoretical value of the probability is {}".format(bin_distr(n_trials, n_successes, p, q)))
