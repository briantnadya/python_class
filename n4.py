def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    n_iter = abs(y)
    i = 0
    result = float(1/x)
    while i < n_iter-1:
        result = result * float(1/x)
        i += 1
    return result


def main():
    pos_float = float(input("Please enter the positive real number: "))
    neg_int = int(input("Please enter the negative integer number: "))
    print("The result of {}^({}) is {}".format(pos_float, neg_int, my_func_2(pos_float, neg_int)))


if __name__ == "__main__":
    main()
