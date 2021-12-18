user_n = int(input("Please enter a positive integer: "))
max_n = 0

while user_n > 0:
    digit = user_n % 10
    if max_n < digit:
        max_n = digit
    user_n = user_n // 10

print("The largest digit in your number is: ", max_n)
