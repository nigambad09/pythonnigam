# CSV
# import CSV
import csv

with open ('data.csv') as a:
    r = csv.reader(a)
    for row in r:
        print(row[0],row[1],sep=" |")
