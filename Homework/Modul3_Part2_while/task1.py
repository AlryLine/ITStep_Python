a = int(input('Input number: '))
b = int(input('Input number: '))
sum1 = a%2
sum2 = not a%2
sum3 = a%9
while a < b:
    if a%2:
        print (sum1)
        a += 1
    elif not a%2:
        print (sum2)
        a += 1
    elif a%9:
        print (sum3)
        a += 1
print ((sum1 + sum2 + sum3) // 3)