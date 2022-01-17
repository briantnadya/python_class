from __future__ import division

class Cell:
    def __init__(self, partition_n):
        self.partition_n = partition_n

    def __add__(self, other):
        return int(self.partition_n + other.partition_n)

    def __sub__(self, other):
        if (self.partition_n - other.partition_n) > 0:
            result = int(self.partition_n - other.partition_n)

        elif (other.partition_n - self.partition_n) > 0:
            result = int(other.partition_n - self.partition_n)

        else:
            print("the difference between the partition number of two cells is less than zero, cannot use __sub__ !")
        return result

    def __mul__(self, other):
        return int(self.partition_n * other.partition_n)

    def __truediv__(self, other):
        if self.partition_n >= other.partition_n:
            result = int(self.partition_n / other.partition_n)

        elif other.partition_n > self.partition_n:
            result = int(other.partition_n / self.partition_n)

        return result

    def make_order(self, cells_in_a_row):
        final_str = ''
        full_rows_n = int(self.partition_n / cells_in_a_row)
        remainder_n = int(self.partition_n % cells_in_a_row)
        for el in range(full_rows_n):
            final_str = final_str + ("*" * cells_in_a_row) + "\n"
        final_str = final_str + ("*" * remainder_n)

        return final_str


obj_1 = Cell(25)
obj_2 = Cell(15)

print("The result of ADD method is {}.\n".format(obj_1 + obj_2))
print("The result of SUB method is {}.\n".format(obj_1 - obj_2))
print("The result of MUL method is {}.\n".format(obj_1 * obj_2))
print("The result of TRUEDIV method is {}.\n".format(obj_1 / obj_2))

print("The result of MAKE_ORDER method is: \n{}".format(obj_1.make_order(4)))
