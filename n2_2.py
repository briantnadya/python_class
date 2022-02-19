import numpy as np
import matplotlib.pyplot as plt

n_samples = 1000
amount_el = 10
sum_list = []

for i in range(n_samples):
    sum_el_samp = 0
    for j in range(amount_el):
        rand_n = np.random.randint(0, 10)
        #print("Random number is {}".format(rand_n))
        #wait = raw_input("press <Enter> to get a random number!")
        sum_el_samp += rand_n
    sum_list.append(sum_el_samp)
    print("The final sum of the sample is {}". format(sum_el_samp))

n, bins, patches = plt.hist(sum_list, n_samples)
plt.xlabel('sum_of_sample')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()