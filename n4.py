import string

class Storage:
    def __init__(self):
        my_dict_amount = {"Printer": 0, "Scanner": 0, "Copier": 0}
        my_dict_dep = {"Printer": "production", "Scanner": "purchasing", "Copier": "delivery"}
        self.warehouse_goods = my_dict_amount
        self.goods_location = my_dict_dep

    def reception_office_eq(self, other):
        if other.__class__.__name__ in self.warehouse_goods.keys():
            counter = self.warehouse_goods.get(other.__class__.__name__)
            try:
                numbers_to_storage = int(raw_input("Please enter how many {} do you wanna send to the storage: ".format(other.__class__.__name__)))
                if type(numbers_to_storage) == int:
                    self.warehouse_goods[other.__class__.__name__] = counter + numbers_to_storage
                return "{} {} has been accepted to the warehouse.\nThe numbers of all the things: {}\n".format(
                    numbers_to_storage, other.name, self.warehouse_goods)
            except ValueError:
                print("You didn't enter the number")

    def moving_eq_to_specific_div(self, other):

        if other.__class__.__name__ == "Printer" or other.__class__.__name__ == "Scanner" or other.__class__.__name__ == "Copier":
            try:
                required_dep = raw_input("Please enter to which department you wanna move {}: ".format(other.__class__.__name__)).strip()
                if not required_dep:
                    raise ValueError
            except ValueError:
                raise ValueError('empty string, please enter the string to change the department.')
            else:
                self.goods_location[other.__class__.__name__] = required_dep
                return "{} has been moved to the purchasing department; resulting data: {}".format(other.name,                                                                                     self.goods_location)
        else:
            return "{} has been moved to the Storage".format(other.name)


class Office_equipment:
    def __init__(self, printer_toner, paper):
        self.printer_toner = printer_toner
        self.paper = paper


class Printer(Office_equipment):
    def __init__(self, name, printer_toner, paper, electronic_data_to_print):
        self.name = name
        self.printer_toner = printer_toner
        self.paper = paper
        self.electronic_data_to_print = electronic_data_to_print


class Scanner(Office_equipment):
    def __init__(self, name, printer_toner, paper, physical_data_to_scan):
        self.name = name
        self.printer_toner = printer_toner
        self.paper = paper
        self.physical_data_to_scan = physical_data_to_scan


class Copier(Office_equipment):
    def __init__(self, name, printer_toner, paper, physical_data_to_copy):
        self.name = name
        self.printer_toner = printer_toner
        self.paper = paper
        self.physical_data_to_copy = physical_data_to_copy


obj_1 = Printer("Printer_1", True, True, True)
obj_2 = Storage()

obj_3 = Scanner("Scanner_1", True, True, True)
obj_4 = Copier("Copier_1", True, True, True)


#print(obj_2.reception_office_eq(obj_1))
#print(obj_2.reception_office_eq(obj_3))
#print(obj_2.reception_office_eq(obj_4))

print(obj_2.moving_eq_to_specific_div(obj_1))
print(obj_2.moving_eq_to_specific_div(obj_3))
print(obj_2.moving_eq_to_specific_div(obj_4))