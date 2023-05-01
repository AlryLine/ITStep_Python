a = int(input('Please, input number: '))
b = int(input('Please, input number: '))

for i in range (a,b+1):
    if (i%3 == 0) and (i%5 != 0):
        print ('Fizz')
print ()
for i in range (a,b+1): 
   if (i%5 == 0) and (i%3 != 0):
        print ('Buzz')
print ()
for i in range (a,b+1):
    if ((i%3 == 0)) and ((i%5 == 0)):
        print ('Fizz Buzz')
print ()
for i in range (a,b+1):
    if ((i%3 != 0)) and ((i%5 != 0)):
        print (i) 
print ()