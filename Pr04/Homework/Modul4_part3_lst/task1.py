n = int(input('Count of number: '))

import random

num_lst_1 = []
num_lst_2 = []
num_lst_all = []
num_lst_bez_povt = []
num_lst_spilni = []
num_lst_unik = []
num_lst_min_max = []

for i in range (n):
     num_lst_1.append (random.randint (1, n))
     num_lst_2.append (random.randint (1, n))
print ('Task1.1: ', sep= ' ')
print (num_lst_1)
print (num_lst_2)

num_lst_all = (num_lst_1 + num_lst_2)
print ('Task1.2: ', sep= ' ')
print (num_lst_all)

for j in num_lst_all:
        if j not in num_lst_bez_povt:
              num_lst_bez_povt.append (j)
print ('Task1.3: ', sep= ' ')
print (num_lst_bez_povt)

for k in num_lst_1 and num_lst_2:
        if k in num_lst_1 and num_lst_2:
               num_lst_spilni.append (k)
print ('Task1.4: ', sep= ' ')
print (num_lst_spilni)

for l in num_lst_1:
       if l not in num_lst_unik:
              num_lst_unik.append (l)
for q in num_lst_2:
       if q not in num_lst_unik:
              num_lst_unik.append (q)
print ('Task1.5: ', sep= ' ')
print (num_lst_unik)

num_lst_min_max.append (min(num_lst_1))
num_lst_min_max.append (max(num_lst_1))
num_lst_min_max.append (min(num_lst_2))
num_lst_min_max.append (max(num_lst_2))

print ('Task1.6: ', sep= ' ')
print (num_lst_min_max)