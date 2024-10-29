class Car :
    name = None
    password = "123"

    def __init__(self):
        self.public_variable = "namepublic"
        self._protect_var = "protected123"
        self.__private_var = "pass123"

    def _protected_method(self): # only allowed prcoted mehod for protected varibale
        print("protected")
    def __private_method(self):
        print("private")
        
    # cannot use private varibale

    def printName(self):
        print(self.public_variable)

suv = Car()
suv.printName() #public can be called
suv._protected_method()  #protected variable cannot be used but by protected mehtod we can use it
# private cannot be used

