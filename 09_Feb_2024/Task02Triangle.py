# Traiangle
s1 = int(input("Enter the side1 of traingle "))
s2 = int(input("Enter the side2 of traingle "))
s3 = int(input("Enter the side3 of traingle "))

if s1 == s2 == s3:
    print("equilateral triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("isosceles  triangle")
else:
    print("scalen triangle ")
