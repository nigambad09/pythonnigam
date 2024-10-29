# Function
# THre are many types of function

# Define function with def with camel case name
def say_hello():  # Non return type /No argument function
    # code
    print("hello nigam")


#    call the function
say_hello()


# No return type with arguments

def say_bye(nigs):
    print(nigs, "man")


say_bye("handsome")

# No return type with arguments with default value
def say_bye(nigs="man"):
    print(nigs, "man")


say_bye()


# return type with arguments
def sum_of_num(a, b):
    return a + b


result = sum_of_num(3, 4)
result2 = sum_of_num("amit","sham")
result3 = sum_of_num(a="hi",b="bye")
print(result)
print(result2)
print(result3)