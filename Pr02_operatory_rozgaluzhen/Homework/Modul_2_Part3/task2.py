print ('Hi! :)')
n = int(input('Input number: '))
print ('Choises: ')
print ('1: n to the power of 0')
print ('2: n to the power of 1')
print ('3: n to the power of 2')
print ('4: n to the power of 3')
print ('5: n to the power of 4')
print ('6: n to the power of 5')
print ('7: n to the power of 6')
print ('8: n to the power of 7')
choice = int(input('Please, input your choice: '))
if choice == 1:
    print (n**0)
elif choice == 2:
    print (n**1)
elif choice == 3:
    print (n**2)
elif choice == 4:
    print (n**3)
elif choice == 5:
    print (n**4)
elif choice == 6:
    print (n**5)
elif choice == 7:
    print (n**6)
elif choice == 8:
    print (n**7)
else:
    print ('Please, input correct number')
print ('Bye!')