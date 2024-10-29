#ENcapsulation


class Car :
    name = None

    def __init__(self,name):
        self.name = name

    def printname(self):
        print(self.name)

xuv = Car("TATA")
xuv.printname()