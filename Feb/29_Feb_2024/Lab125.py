# Abstraction
# Hidiing the details and showing the what is requireed

# Abstract Class and Abstract Methods
# in Java anstract class and interface
# in python abstract class and method

# ABC is abst
from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("bow bow")

class Cat(Animal):
    def sound(self):
        print("mewo mewo ")


d= Dog("mascow")
d.sound()
c = Cat("chiu")
c.sound()