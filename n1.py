import numpy as np

amount_n = input("Please enter how many random numbers do you wanna to generate: ")

for i in range(amount_n):
    rand_n = np.random.randint(0, 36)
    wait = raw_input("press <Enter> to get a random number!")
    print("Your number {} of the roulette field is: {}".format(i+1, rand_n))


