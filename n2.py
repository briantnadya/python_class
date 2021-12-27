init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
final_list = [el for el in init_list[1:] if el > init_list[init_list.index(el) - 1]]
print(final_list)
