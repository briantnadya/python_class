from functools import reduce


def mult_func(prev_elem, elem):
    return prev_elem * elem


def fact(number):
    yield reduce(mult_func, range(1, number+1))


n = int(input("Please enter the number to calculate the factorial: "))

i = 1
while i <= n:
    for el in fact(i):
        print("Factorial of {} is {}".format(i, el))
    i += 1

