initial_list = [7, 5, 3, 3, 2]
max_n_elem = 10

while len(initial_list) != max_n_elem: #to not run the program multiple times

    user_input = int(input("Please enter the positive integer: "))

    if user_input in initial_list:
        ind_el = initial_list.index(user_input)
        initial_list.insert(ind_el + 1, user_input)

    elif user_input > max(initial_list):
        initial_list.insert(0, user_input)

    elif user_input < min(initial_list):
        initial_list.append(user_input)

    print(initial_list)
