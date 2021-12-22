struct_final = []
temp_tuple = ()
count = 1
max_count = int(input("Please enter how many items do you want to enter: "))

while count != max_count+1:
    user_name = raw_input("Please enter the name of an item {}: ".format(count))
    user_price = float(input("Please enter the price of this item: "))
    user_amount = float(input("Please enter the number of these items: "))
    user_unit = raw_input("Please enter an unit of this item: ")
    temp_tuple = (count, {"name": user_name, "price": user_price, "amount": user_amount, "unit": user_unit})
    count = count + 1
    struct_final.append(temp_tuple)

print(struct_final)
amounts_list = []
names_list = []
prices_list = []
unites_list = []

for elem in struct_final:
    amounts_list.append(elem[1].get("amount"))
    names_list.append(elem[1].get("name"))
    prices_list.append(elem[1].get("price"))
    unites_list.append(elem[1].get("unit"))

info_dict = {struct_final[0][1].keys()[0]: amounts_list, struct_final[0][1].keys()[1]: prices_list, struct_final[0][1].keys()[2]: amounts_list, struct_final[0][1].keys()[3]: names_list}
print(info_dict)

