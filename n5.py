class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Starts drawing!")


class Pen(Stationery):
    def draw(self):
        print("You are using a {} pen. Be careful, it cannot be erased!".format(self.title))


class Pencil(Stationery):
    def draw(self):
        print("You are using a {} pencil. Prepare your eraser!".format(self.title))


class Handle(Stationery):
    def draw(self):
        print("You are using a {} handle. Good for drawing graffiti!".format(self.title))


obj_1 = Pen("KAUST")
obj_1.draw()

obj_2 = Pencil("BIC")
obj_2.draw()

obj_3 = Handle("Staedtler")
obj_3.draw()
