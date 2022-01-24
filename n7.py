class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return "The result of the sum of two complex numbers: {} + ({}i)".format(int((self.real_part + other.real_part)), int((self.imaginary_part + other.imaginary_part)))

    def __mul__(self, other):
        return "The result of multiplication of two complex numbers: {} + ({}i)".format(int((self.real_part * other.real_part)) - int((self.imaginary_part * other.imaginary_part)), int((self.real_part * other.imaginary_part)) + int((self.imaginary_part * other.real_part)))


obj1 = ComplexNumber(2, -5)
obj2 = ComplexNumber(3, 4)

print(obj1 + obj2)
print(obj1 * obj2)


