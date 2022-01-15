class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        my_dict = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = my_dict


class Position(Worker):
    def get_full_name(self):
        print("Full name is: {} {}".format(self.name, self.surname))

    def get_total_income(self):
        print("An income of {} equals: {}\n".format(self.position, int(self._income.get("wage") + self._income.get("bonus"))))


worker_1 = Position("Peter", "Parker", "Spider Man", 10000, 40000)
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position("Mary", "Jane", "Waitress", 1000, 400)
worker_2.get_full_name()
worker_2.get_total_income()

