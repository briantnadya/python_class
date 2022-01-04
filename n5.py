
filedata = '12 34 5 4 2 1 6 7'

with open('n4_num_list.txt', 'w') as file:
    file.write(filedata)

with open('n4_num_list.txt', 'r') as file:
    filedata = [int(el) for el in file.read().split()]

print('Sum of the numbers is {}'.format(sum(filedata)))