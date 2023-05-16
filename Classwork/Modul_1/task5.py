a = int(input('Input n: '))
b = int(input('Input n: '))
if a>=b:
    a,b=b,a
while a <= b:
    if a%2!=0:
     print(a, end=' ')
    a += 1