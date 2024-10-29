# Inhertance

class Father:
    def car(self):
        print("lembo")

    def flat(self):
        print("2bhk")

class Son(Father):
    pass

a = Son()
a.car()
a.flat()