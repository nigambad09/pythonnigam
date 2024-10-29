set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
my_set = set1.union(set2)
print(my_set)
# {1, 2, 3, 4, 5, 6, 7}

my_set2 = set1.intersection(set2)
print(my_set2)
# {4, 5

my_set2 = set1.difference(set2)
print(my_set2)
# {1, 2, 3}

my_set2 = set1.issubset(set2)
print(my_set2)
# False