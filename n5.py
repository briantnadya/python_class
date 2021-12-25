import re

Flag = True
result = 0
special_characters = "!@#$%^&*()-+?_=,<>/"

while Flag:
    user_numbers = raw_input("Please enter the numbers to sum: ")

    if any(character in special_characters for character in user_numbers):
        if (character.isdigit() for character in user_numbers):
            numb_list = [int(re.sub('[^0-9]+', '', _)) for _ in user_numbers.split()]

        else:
            print("You wrote only special characters!")

        Flag = False

    else:
        numb_list = list(map(int, user_numbers.split()))

    result = result + sum(numb_list)
    print("The sum of all of the numbers you entered: {}".format(result))