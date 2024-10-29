# deifference between argsand kwargs
def print_args(*numbo):
    for i in numbo:
        print(i,end=" ")

print_args(1)
print_args("nigam")
print_args(1,2,3)

def print_multiple(*a,c):
        print(a,c)

print_multiple(2, 3, 4, 5, c="f")