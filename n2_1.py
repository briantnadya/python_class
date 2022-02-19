import numpy as np

amount_n = input("Please enter how many random numbers do you wanna to generate: ")
red_fields = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]

# number of even fields among red fields
n_even_fields = 9.0

# number of red fields
n_red_fields = 18.0

# number of all the fields
n_fields = 36.0
k = 0.0

for i in range(amount_n):
    rand_n = np.random.randint(1, 36)
    # wait = raw_input("press <Enter> to get a random number!")
    if rand_n in red_fields and (rand_n % 2 == 0):
        k = k + 1
    # print("Your number {} of the roulette field is: {}".format(i + 1, rand_n))

print(float(k) / amount_n)
print("The probability that you get red and even field is {}.".format(
    (n_even_fields / n_red_fields) * (n_red_fields / n_fields)))
