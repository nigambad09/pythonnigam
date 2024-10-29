# Method Overloading
# python doesnt support it in traditional sense its same name of function in different parameter

class Maths:
    def add(self,a,b=0,c=0):
        return a+b+c
    # def add(self,a,b):
    #     return a+b
# doesnt support
M = Maths
print(M.add(1,2))