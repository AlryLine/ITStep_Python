n = int(input('Input number: '))

while n!=7:
    if n>0:
        print ('Number is positive')
    elif n<0:
        print ('Number is negative')
    elif n == 0:
        print ('Number is equal to zero')
        n = int(input('Input number: '))
else:
    print ('Good Bye!')