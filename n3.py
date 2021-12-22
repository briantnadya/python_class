seasons_dict = {"Winter": [12, 1, 2], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
n_month = int(input("Please enter the number of a month (positive integer from 1 to 12: "))
dict_items = seasons_dict.items()

while n_month < 1 or n_month > 12:
    n_month = int(input("Please enter the number of a month (positive integer from 1 to 12: "))


for item in dict_items:
    for elem in item[1]:
        if elem == n_month:
            print("It's {}!".format(item[0]))


