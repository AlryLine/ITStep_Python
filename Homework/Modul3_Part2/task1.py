a = int(input('Input number: '))
b = int(input('Input number: '))
sum1 = 0
sum2 = 0
sum3 = 0
while a < b:
    sum2 += a if a%2 else 0
    sum1 += a if not a%2 else 0
    sum3 += a if a%9 else 0
    a += 1
print (sum1, sum2, sum3)
print ((sum1 + sum2 + sum3) // 3)
    

