print ('Hi!')
m = float(input('Input number of meters: '))
print ('Choices: ')
print ('1: miles')
print ('2: inches')
print ('3: yards')
mi = m * 0.00062137
inch = m * 39.3701
yd = m * 1.0936
choice = int(input('Your choice: '))
if choice == 1:
    print (mi)
elif choice == 2:
    print (inch)
else:
    print (yd)
print ('Thank you, bye!')