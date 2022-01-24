from __future__ import division


class SpecialError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data_n = input("Please enter the numerator: ")
inp_data_d = input("Please enter the denominator: ")

try:
    float(int(inp_data_n)/int(inp_data_d))
except ValueError:
    print("You didn't enter the number")
except ZeroDivisionError:
    print("Everything is good with the entered numbers!")