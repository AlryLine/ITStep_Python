print ('Hello! :)')
a = int(input('Input number: '))
b = int(input('Input number: '))
c = int(input('Input number: '))
print ('Choices: ')
print ('1: sum')
print ('2: m')
choice = int(input('Input your choice: '))
if choice == 1:
    print (a + b + c)
elif choice == 2:
    print (a * b * c)
else:
    print ('Error')
print ('Thanks, have a hice day!')