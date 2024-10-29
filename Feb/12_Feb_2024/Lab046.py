
# Triangle classifier
# side 1 ==side2==side 3 = equilater
#

side1 = float (input("enter the side 1\n"))
side2 = float (input("enter the side 2\n"))
side3 = float (input("enter the side 3\n"))

if side1 == side2 ==side3 :
    print("Eqilater")
elif side1 == side2 or side1 == side3 or side2 == side3 :
    print("ISO")
else:
    print("scalen")