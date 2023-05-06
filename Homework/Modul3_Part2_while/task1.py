a = int(input('Input number: '))
b = int(input('Input number: '))
sum1 = 0
sum2 = 0
sum3 = 0
while a < b:
    if a%2 == 0:
        print (sum1)
        a += 2
    elif a%2 != 0:
        print (sum2)
        a += 1
    elif a %9 == 0:
        print (sum3)
        a += 1
    a += 1
print (sum1)
print (sum2)
print (sum3)
print ((sum1 + sum2 + sum3) // 3)