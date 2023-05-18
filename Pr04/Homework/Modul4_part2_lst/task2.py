n = int(input('Count of number: '))

import random

num_lst = []
for i in range (n):
     num_lst.append (random.randint(-5, n))

count1 = 0
count2 = 0
count3 = 0
for i in num_lst:
    if i < 0:
        count1 += 1
    elif i > 0:
        count2 += 1
    elif i == 0:
        count3 += 1

print (num_lst)
print ('Negative numbers: ', (count1))
print ('Positive numbers: ', (count2))
print ('Numbers equal to zero: ', (count3))
print ('Max number: ', max(num_lst))
print ('Min number: ', min(num_lst))