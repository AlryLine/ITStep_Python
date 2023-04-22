print ('Welcome!')
t = int(input('Input call cost: '))
print ('Choice mobile operators: ')
print ('1: Kyivstar -> Kyivstar')
print ('2: Lifecell -> Lifecell')
print ('3: Kyivstar -> Lifecell')
print ('4: Lifecell -> Kyivstar')

choice = int(input('Your choice: '))
if t == 1:
    print ('1.5grn/min')
elif t == 2:
    print ('1.46grn/min')
elif t == 3:
    print ('2.5grn/min')
elif t == 4:
    print ('2.78grn/min')
s = choice * t
print (s)
print ('Thanks, goodbye!')