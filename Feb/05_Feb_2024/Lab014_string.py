
str1 = "nigam"
str2 ='nigam'
print(str1 + str2)
print(type(str1))
print(type(str2))

#difference in single quote and double quote
dir1 ="C:/abc\abc.txt"
dir2 ='C:\abc\abc.txt'
print (dir1)
print (dir2)
#\a has some meaning so to avoid this use r"" ""as raw
dir3 =r"C:/abc\abc.txt"
print (dir3)

#format string f""
s= "Amit"
print(f"Your name is {s}")

#format table o f2
num = 2
print (f"{num}*1 ={num*1}")
print (f"{num}*2 ={num*2}")
print (f"{num}*3 ={num*3}")
print (f"{num}*4 ={num*4}")