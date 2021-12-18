revenue = float(input("Please enter the revenue of your company (positive number): "))
costs = float(input("Please enter the company costs (positive number): "))

if revenue > costs:
    print("Your company is in a profit this time! Keep going :) ")
    employees_n = int(input("Please enter the number of employees to compute the profitability of proceeds: "))
    prof_per_emp = float(revenue/employees_n)
    print('Profitability of proceeds per each employee is {}'.format(prof_per_emp))
else:
    print("Your company is at a loss! It's time for changes! ")