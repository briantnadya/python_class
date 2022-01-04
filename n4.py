# -*- coding: utf-8 -*-

with open("n4_numbers.txt", "r") as file:
    filedata = file.read()

filedata = filedata.replace('One', 'Один')
filedata = filedata.replace('Two', 'Два')
filedata = filedata.replace('Three', 'Три')
filedata = filedata.replace('Four', 'Четыре')

with open('n4_numbers_updated.txt', 'w') as file:
    file.write(filedata)