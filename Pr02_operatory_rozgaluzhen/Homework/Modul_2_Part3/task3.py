print ('Welcome!')
t = int(input('Input call cost: '))
print ('Choice mobile operators: ')
print ('1: Kyivstar -> Kyivstar')
print ('2: Lifecell -> Lifecell')
print ('3: Kyivstar -> Lifecell')
print ('4: Lifecell -> Kyivstar')
t1 = 1.5 #grn/min
t2 = 1.36 #grn/min
t3 = 2.5 #grn/min
t4 = 2.78 #grn/min
choice = int(input('Your choice: '))
if choice == 1:
    print (t * t1)
elif choice == 2:
    print (t * t2)
elif choice == 3:
    print (t * t3)
elif choice == 4:
    print (t * t4)
else:
    print ('Error!')
print ('Thanks, goodbye!')