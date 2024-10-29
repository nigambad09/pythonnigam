# Map

def sq_number(num):
    return num**2

# result i will get square of number

number =[1,2,3,4,5]
# 'Map'
# Take a number from list and use in function sq_number
output = list(map(sq_number,number))
print(output)

import math

def sq_rt(num):
    return math.sqrt(num)

mylist = [4,16,25,64]

sq = list(map(sq_rt,mylist))
print(sq)