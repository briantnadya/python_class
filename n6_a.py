from itertools import count


"""a) part of the task 6"""
user_input = int(input("Please enter an integer number you wanna start with: "))
max_number = 10

for el in count(user_input):
    if el > max_number:
        break
    else:
        print(el)
