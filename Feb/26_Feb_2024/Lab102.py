class Person :
    name = "sham"
    age = 23
        #Class variable /Instance varibale

    def walk(self):
        a = 10 # local varible
        print("HElllo my name is", self.name)
        print("Hello my age is",self.age)

amit = Person()
amit.walk()