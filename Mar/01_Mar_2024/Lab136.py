# customise error by MycustomException class
class MyCustomException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance =100
withdrwa_amt = int(input("enter the amount to withdraw"))

if withdrwa_amt > balance :
    raise MyCustomException("Balance is low")
else:
    print(withdrwa_amt)