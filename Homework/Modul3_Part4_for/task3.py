a = int(input('Input number: '))
b = int(input('Input number: '))

while a <= b:
    for i in range (1, 11):
        print (a, '*', i, '=', a*i)
    a += 1
    print ()