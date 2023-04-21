print ('Hey! :)')
a = int(input('Input number: '))
b = int(input('Input number: '))
c = int(input('Input number: '))
print ('Choices: ')
print ('1: max')
print ('2: min')
print ('3: average')
mx = max (a, b, c)
mn = min (a, b, c)
average = (a + b + c)/3
choice = int(input('Input your choice: '))
if choice == 1:
    print (mx)
elif choice == 2:
    print (mn)
else: 
    print(average)    
print ('Bye!')