# We can use both value as error as e or execption as e
# Exception is parent to all exception
# Value error is specific error

try:
    a = int(input("Enter the num 1\n"))
    b = int(input("Enter the num 2\n"))
    c = a/b
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
else:
    print("div of value is ", c)
finally:
    print("i wil be execute any how")