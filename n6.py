import json

with open("subjects_data.json") as read_f:
    data = json.load(read_f)

data_dict = {}

for key, values in data.items():
    for word in key.encode('ascii', 'ignore').split('\n'):
        hours_list = []
        for states, hours in data[word].items():
            hours_list.append(hours)
        data_dict[word] = sum(hours_list)

print(data_dict)

