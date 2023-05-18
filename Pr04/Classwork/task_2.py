n = int(input('Count of num: '))
lst = []

for i in range (n):
    lst.append (int(input('number [' + str(i) +'] = ')))
number = int(input('n = '))
count = lst.count (number)
print (count)