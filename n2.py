class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def fabric_consumption(self):
        return float(self.size / 6.5) + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def fabric_consumption(self):
        return float(2 * self.height) + 0.3


# abstract class for checking @property feature
class Dress(Clothes):
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    @property
    def my_method(self):
        return "{} has the following size and height: {}, {}.".format(self.name, self.size, self.height)


obj_1 = Coat("Black coat", 44)
print("{} fabric consumption is {}. \n".format(obj_1.name, obj_1.fabric_consumption()))

obj_2 = Suit("White suit", 154)
print("{} fabric consumption is {}. \n".format(obj_2.name, obj_2.fabric_consumption()))

print("Overall fabric consumption is {}. \n".format(float(obj_1.fabric_consumption() + obj_2.fabric_consumption())))

obj_3 = Dress("Small red dress", 42, 154)
print(obj_3.my_method)