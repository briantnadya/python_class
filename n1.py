def salary_calc(output_in_hours, rate_per_hour, bonus):
    return float(output_in_hours * rate_per_hour + bonus)


def main():
    info_list = ["output in hours", "rate per hour", "bonus"]

    user_input = [float(input("Please enter {} to calculate the salary: ".format(item))) for item in info_list]
    print("Your salary is {}".format(salary_calc(*user_input)))


if __name__ == "__main__":
    main()
