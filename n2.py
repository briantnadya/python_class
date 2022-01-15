class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calculation(self, mass_asp_square_meter, width_cm):
        mass_asp = float(self._length) * float(self._width) * float(mass_asp_square_meter) * float(width_cm)
        print("The mass of the asphalt is: {}".format(mass_asp))


mass_asp_square_meter = float(input("Please enter the mass of an asphalt per 1 square meter, 1cm width: "))
width_cm = float(input("Please enter the number cm of canvas thickness: "))

object_road = Road(10, 20)
object_road.asphalt_mass_calculation(mass_asp_square_meter, width_cm)
