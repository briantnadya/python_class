def division_func(a, b):
    if b == 0:
        print("Cannot divide by zero, please try again.")
    else:
        return a / b


def main():
    user_number_a = float(input("Please enter the 1st number: "))
    user_number_b = float(input("Please enter the 2nd number: "))
    print("The result is: {}".format(division_func(user_number_a, user_number_b)))


if __name__ == "__main__":
    main()
