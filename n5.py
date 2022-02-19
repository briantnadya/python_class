import numpy as np

n = 10
r = 0.9
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)


def corr_coeff(x, y):
    sum_num = 0
    sum_den = 0
    sum_x_2 = 0
    sum_y_2 = 0
    for i in range(0, len(x)):
        sum_num += (x[i] - x.mean()) * (y[i] - y.mean())
        sum_x_2 += (x[i] - x.mean()) ** 2
        sum_y_2 += (y[i] - y.mean()) ** 2
    sum_den = np.sqrt(sum_x_2 * sum_y_2)
    return float(sum_num) / sum_den


# let's compute the correlation coefficient
R = corr_coeff(x, y)

# we can compare the results by calculating the following coefficient C
C = np.corrcoef(x, y)
print("The resulting correlation coefficient is {}".format(R))
print(C)
