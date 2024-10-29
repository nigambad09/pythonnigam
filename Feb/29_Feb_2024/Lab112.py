# Single -80 % use this type
# Multiple
# Multi level
# Hybrid
# Herarchay

# Multipe

class Grandfather :
    def grand_father(self):
        return "grandfather prperty"

class Father(Grandfather):
    def father(self):
        print("father property")

class Son(Father):
    def son(self):
        print("son property")

a = Son()
print( a.grand_father() )
a.father()

