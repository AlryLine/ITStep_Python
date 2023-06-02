import random

lst1 = []
lst2 = []
for i in range (5):
    lst1.append (random.randrange(1, 20, 1))
    lst2.append (random.randrange(1, 20, 1))
print (lst1)
print (lst2)

def add_lists (lst1, lst2):
    lst3 = lst1 + lst2
    return lst3
print (add_lists (lst1, lst2))