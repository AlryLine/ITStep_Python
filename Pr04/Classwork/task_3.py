n = int(input('Count of number: '))
lst = []
for i in range (n):
    lst.append (int(input('number [' + str (i) + '] = ')))
print (sum(lst))
print((sum(lst))/n)