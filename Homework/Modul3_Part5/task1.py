print ('Hello!')
print ('Choises: ')
print ('1: a')
print ('2: b')

choice = int(input('Your choice: '))
if choice == 1:
    n = int(input('Number: '))
    for i in range (n):
        print (' '*i, '*'*(n - i), sep= ' ')
elif choice == 2:
    n = int(input('Number: '))
    for i in range (n):
        print ('*'*(i + 1), ' '*(n - i), sep= ' ')