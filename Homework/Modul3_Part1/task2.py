a = int(input('Please, input number: '))
b = int(input('Please, input number: '))

for i in range (a,b+1,1):
    print (i, end=' ')
print ()
for i in range (b,a-1,-1): 
    print (i, end=' ')
print () 
for i in range (a,b+1):
    if i%7 ==0: 
        print (i, end=' ') 
print () 
for i in range (a,b+1):
    if i%5 ==0: 
        print (i, end=' ') 
print ()
