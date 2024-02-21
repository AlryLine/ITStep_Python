print ('Welcome!')
a = int(input('Input number: '))
b = int(input('Input number: '))
if a == b:
    print ('Numbers are equal')
else:
    while a <= b:
        print (a, end=' ')
        a += 1
print ('Great, bye!')