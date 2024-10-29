# Multiple inhertiance father mother >>sun

class Father:
    def father_money(self):
        print("father money")
    def home(self):
        print("This is from father")

class Mother:
    def mother_money(self):
        print("mother money ")
    def home(self):
        print("This is from mother")

class Son(Father,Mother):
    pass

a = Son()
a.mother_money()
a.father_money()
a.home()
# MRO method resolution order