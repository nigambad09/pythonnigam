# File Handeling
# How to reead a text and write into it using python COde

# Function
# - open ("file_name","mode")
# mode -
# r - for reading
# w - for writing
# a - append
# b - binary mode  .exe file
# + - for updating (reading and writing

# Read and write
# Reading Entire  content : content = file_object.read()
# line = for a single line : file_object.redline()
# lines =  for all lines in a last: file_object.readlines()
# close the file
#

file = open("TestData.txt",'r')
# with open("TestData.txt",'r') as file
content = file.read()
print(content)
file.close()