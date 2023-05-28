import random

numbers = []
for i in range (5):
     numbers.append (random.randrange(1, 5, 1))
print (numbers)

minimum = min(numbers)
def min_of_five_nums (numbers):
     print (minimum)


min_of_five_nums (minimum)

# Або:

def min_of_five_numbers (numbers):
    minimum = numbers [0]
    for i in range (len(numbers)):
        if numbers [i] < minimum:
            minimum = numbers [i]
    return print (minimum)

min_of_five_numbers ([8, 4, 5, 7, 9])