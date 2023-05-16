print ('Hello! :)')
n = int(input('Input number: '))

for i in range (2, n):
    if n % i == 0:
        print ('Not a prime number')
        break
else:
    print ('Prime number')
print ('Good bye!')
print (':)')