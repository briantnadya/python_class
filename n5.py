from functools import reduce


def mult_func(prev_el, el):
    return prev_el * el


result_list = [el for el in range(100, 1001) if el % 2 == 0]

print("The result of the multiplication of all of the even numbers from 100 to 1000 is {}".format(reduce(mult_func, result_list)))
