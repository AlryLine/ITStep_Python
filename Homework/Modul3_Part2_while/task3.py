n = int(input('Input number: '))

while n != 7:
    if n > 0:
        print ('Number is positive')
        n = int(input('Input number: '))
    elif n < 0:
        print ('Number is negative')
        n = int(input('Input number: '))
    elif n == 0:
        print ('Number is equal to zero')
        n = int(input('Input number: '))
else:
    print ('Good Bye!')