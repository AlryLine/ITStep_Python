a = int(input('Input n: '))
b = int(input('Input n: '))
sum = 0
i = 0
while a <= b:
    print(a, end=' ' )
    sum += a
    i += 1
    a += 1
else:
    print('summa: ', sum)
    print('arithmetic mean: ', sum/i)