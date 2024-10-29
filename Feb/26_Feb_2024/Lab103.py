class Car :
    #class varible
    name = None
    make = None
    model = None

    def __init__(self,o_name,o_make,o_model) : #constructer with parameter
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def car_type(self):
        print("Car name",self.name)
        print("Car make", self.make)
        print("Car model", self.model)

call = Car("lambo","v2",2023) #parameter value
call.car_type()
print("------------------")
call2 = Car("tata","v2",2025) #parameter value
call2.car_type()

