a = int(input('Введіть перший діапазон: '))
b = int(input('Введіть другий діапазон: '))
n = int(input('Введіть число: '))
while not a<n<=b:
    n = int(input('Введіть повторно число: '))
for i in range(a,b+1):
    print
