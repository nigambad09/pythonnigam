# Hierarchical
class Vehicel:
    def vehicel_info(self):
        return "This is car"

class Tata(Vehicel):
    def tata_car(self):
        return "its tata car"

class Mahindra(Vehicel):
    def mhindra_car(self):
        return "its mahindra car"

a = Tata()
b = Mahindra()

print(a.vehicel_info() )
print(a.tata_car() )
print(b.vehicel_info() )
print(b.mhindra_car() )


N