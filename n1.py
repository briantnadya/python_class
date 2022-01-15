import time


class TrafficLight:
    def __init__(self):
        self.__color = ["red", "yellow", "green"]

    def running(self):
        for el in self.__color:
            if el == "red":
                print("Red is working now, stop!")
                time.sleep(7)
            elif el == "yellow":
                print("Yellow is working now, wait!")
                time.sleep(2)
            else:
                print("Green is working now, you can go.".format(self.__color))
                time.sleep(3)


example_1 = TrafficLight()
example_1.running()
