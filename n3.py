def my_func(a, b, c):
    if a >= b >= c or b >= a >= c:
        result = int(a + b)
    elif b >= c >= a or c >= b >= a:
        result = int(b + c)
    else:
        result = int(c + a)
    return result


def main():
    user_numbers = []
    for i in range(3):
        user_n = int(input("Please enter the number {}: ".format(i + 1)))
        user_numbers.append(user_n)

    print("The sum of two maximum numbers: {}".format(
        my_func(user_numbers[0], user_numbers[1], user_numbers[2])))


if __name__ == "__main__":
    main()
