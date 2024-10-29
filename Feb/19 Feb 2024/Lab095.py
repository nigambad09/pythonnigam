class Person:
    # Attribute > Data Memeber AD
    name = None
    age = None
    id = None

    # Bheaviour is Methods (not the function)
    def talk(self):
        print("i can talk")
    # self is used for instance of class
    def walk(self):
        print("i can walk and i am method")


def func():
    print("i am function i am outside class i am indipendent ")


# Object creation  - Variable = classname()

a = Person()
b = Person()

a.id = "123"
a.name = "sham"

a.walk()
print(a.id)
