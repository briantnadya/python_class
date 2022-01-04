
temp_list = []
firms_dict = {}
avg_dict = {}

with open('n7_firms_data.txt', 'r') as my_f:
    for line in my_f:
        if line != '\n':
            words = line.split()
            proceeds = int(int(words[2]) - int(words[3]))
            firms_dict[words[0]] = proceeds
            if proceeds > 0:
                temp_list.append(proceeds)

avr_profit = sum(temp_list)/len(temp_list)

temp_list = []
print("Average profit equals: {}".format(avr_profit))

avg_dict["average_profit"] = avr_profit

temp_list.append(firms_dict)
temp_list.append(avg_dict)
print(temp_list)