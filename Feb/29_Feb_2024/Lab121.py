#Metho overriding- same name in parent and child
# child always override parent
# super means call my parent function
# Multiple inhertiance father mother >>sun

class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print(" dog sound ")


a = Dog()
a.sound() # child override parent

