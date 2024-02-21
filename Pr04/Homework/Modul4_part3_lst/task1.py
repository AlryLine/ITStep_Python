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
print ('Два списки з випадковими числами: ', sep= ' ')
print (num_lst_1)
print (num_lst_2)

num_lst_all = (num_lst_1 + num_lst_2)
print ('Список, який містить елементи обох списків: ', sep= ' ')
print (num_lst_all)

for j in num_lst_all:
        if j not in num_lst_bez_povt:
              num_lst_bez_povt.append (j)
print ('Список, який містить елементи двох списків без повторів: ', sep= ' ')
print (num_lst_bez_povt)

for k in num_lst_1 and num_lst_2:
        if k in num_lst_1 and num_lst_2:
               num_lst_spilni.append (k)
print ('Список, який містить спільні елементи для обох списків: ', sep= ' ')
print (num_lst_spilni)

for l in num_lst_1:
       if l not in num_lst_2 and l not in num_lst_unik:
              num_lst_unik.append (l)
for q in num_lst_2:
       if q not in num_lst_1 and q not in num_lst_unik:
              num_lst_unik.append (q)
print ('Список, який містить унікальні елементи кожного із списків: ', sep= ' ')
print (num_lst_unik)

num_lst_min_max.append (min(num_lst_1)) 
num_lst_min_max.append (max(num_lst_1))
num_lst_min_max.append (min(num_lst_2))
num_lst_min_max.append (max(num_lst_2))

print ('Список, який містить мінімальне та максимальне значення кожного із списків: ', sep= ' ')
print (num_lst_min_max)