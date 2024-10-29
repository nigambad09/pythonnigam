# try except and else finally
# multiple Exception

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