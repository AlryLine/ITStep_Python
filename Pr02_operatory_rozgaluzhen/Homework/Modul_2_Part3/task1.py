print ('Hello!')
n = int(input('Please, input number: '))
if (n < 1) or (n > 100):
    print ('Error')
elif (n%3 == 0) and (n%5!=0):
    print ('Fizz')
elif (n%5 == 0) and (n%3!=0):
    print ('Buzz')
elif ((n%3 == 0)) and ((n%5 == 0)):
    print ('Fizz Buzz')
elif ((n%3 != 0)) and ((n%5 != 0)):
    print (n)
print ('Bye!')