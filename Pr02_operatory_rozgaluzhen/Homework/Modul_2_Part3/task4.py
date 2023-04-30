a = int(input('Рівень продажу першого менеджера: '))
b = int(input('Рівень продажу другого менеджера: '))
c = int(input('Рівень продажу третього менеджера: '))
s = 200 #stavka
if a > 1000:
    zp1 = s + a * 0.08
    print (zp1)
elif a < 500:
    zp1 = s + a * 0.03
    print (zp1)
else:
    zp1 = s + a * 0.05
    print (zp1)
if b > 1000:
    zp2 = s + b * 0.08
    print (zp2)
elif b < 500:
    zp2 = s + b * 0.03
    print (zp2)
else:
    zp2 = s + b * 0.05
    print (zp2)
if c > 1000:
    zp3 = s + c * 0.08
    print (zp3)
elif c < 500:
    zp3 = s + c * 0.03
    print (zp3)
else:
    zp3 = s + c * 0.05
    print (zp3)
if zp1 > zp2 and zp1 > zp3:
    print ('Кращий з продажу - перший менеджер')
    print (zp1 + 200) 
elif zp2 > zp1 and zp2 > zp3:
    print ('Кращий з продажу - другий менеджер')
    print (zp2 + 200)
else:
    zp3 > zp1 and zp3 > zp2
    print ('Кращий з продажу - третій менеджер')
    print (zp3 + 200)

