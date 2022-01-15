class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The car {} is running!".format(self.name))

    def stop(self):
        print("The car {} is stopped.".format(self.name))

    def turn(self, direction):
        print("The car {} turned {}.".format(self.name, direction))

    def show_speed(self):
        print("The speed of {} car is {}.\n".format(self.name, self.speed))


class TownCar(Car):
    def print_name(self):
        print("This is a town car {}.".format(self.name))

    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            print("You are speeding!\n")
        else:
            print("Speed is okay.\n")


class SportCar(Car):
    def print_name(self):
        print("This is a sport car {}.".format(self.name))


class WorkCar(Car):
    def print_name(self):
        print("This is a work car {}.".format(self.name))

    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            print("{} is speeding!\n".format(self.name))
        else:
            print("Speed of {} is okay.\n".format(self.name))


class PoliceCar(Car):
    def print_name(self):
        print("This is a police car {}.".format(self.name))


obj_1 = TownCar(50, "silver", "lincoln", False)
obj_1.print_name()
obj_1.go()
obj_1.stop()
obj_1.turn("left")
obj_1.show_speed()

obj_2 = WorkCar(78, "black", "toyota", False)
obj_2.print_name()
obj_2.go()
obj_2.stop()
obj_2.turn("right")
obj_2.show_speed()

obj_3 = SportCar(200, "red", "ferrari", False)
obj_3.print_name()
obj_3.go()
obj_3.stop()
obj_3.turn("left")
obj_3.show_speed()

obj_4 = PoliceCar(150, "white", "Ford", True)
obj_4.print_name()
obj_4.go()
obj_4.stop()
obj_4.turn("right")
obj_4.show_speed()




