# poly many
# forms- types
# Overloading and Overriding

class Myself:
    def nigam(self):
        print("Its a boy")

class Brother(Myself):
    def nigam(self):
        print("He is a brother")

class BF(Myself):
    def nigam(self):
        print("He is a BF")

rel1 = Myself()
rel1.nigam()
rel2 = BF()
rel2.nigam()