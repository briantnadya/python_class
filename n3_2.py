import math as math


def factorial(n):
    result = 1
    if n > 0:
        for i in range(1, n + 1):
            result = result * i
    elif n == 0:
        result = 1
    else:
        print("Please enter different from negative number.")
    return result


def binomial_c(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


n_trials = int(raw_input("Please enter the number of trials you wanna to do: "))
k_successes = int(raw_input("Please enter the number of successes you desire to get: "))
p = 0.5
q = 1 - p

# let's compute the probability of k_successes out of n_trials assuming "eagle and tail" simulation
prob_final = binomial_c(n_trials, k_successes) * math.pow(p, k_successes) * math.pow(q, n_trials - k_successes)

print(prob_final)
