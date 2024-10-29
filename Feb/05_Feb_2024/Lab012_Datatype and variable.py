#take two number from user and we want to add them
# STep 1 = Take input
#step 2 = sum
num1 = input("Enter the first number")
num2 = input ("Enter the second number")
print(num1)
print(num2)
print(type(num1))
num3 = int(num2) + int(num1)
#str > int use int()
print(type(num1))
#int > str use str()
print(num3)
#input function take data as string only we need to convert into string
# 2 ways to convert into int
#at input level
#num1 =int(input("enter number"))