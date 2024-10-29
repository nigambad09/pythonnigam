# Handel Eccepttion
# try and except block
#     try - try the code
#     except - execute the code

a = int(input("Enter the num 1\n"))
b = int(input("Enter the num 2\n"))

try:
    c = a/b
    print("DEv of num is",c)
except Exception as e:
    print(e)
    print("dont use b as 0")

print("Imortant message is we need to shhow to user")