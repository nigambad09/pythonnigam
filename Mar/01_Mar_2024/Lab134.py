# use class
# custome message in error

class XYZ:
    def f1(self):
        try:
            a = int(input("enter a number"))
        except Exception as e:
            print("customise error message Enter only Int")
        else:
            print(a)
        finally:
            print("end")

a = XYZ()
a.f1()