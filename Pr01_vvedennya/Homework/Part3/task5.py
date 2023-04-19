n = int(input('Your number: '))
a = n % 10
b = n % 100 // 10
c = n // 100 % 10
d = n // 1000
a,b,c,d = d,c,b,a
print (d,c,b,a)