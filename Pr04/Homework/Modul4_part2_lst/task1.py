n = input('Введіть арифметичний вираз: ')

if '+' in n:
    a, b = n.split()
    print(int(a) + int(b))
elif '-' in n:
    a, b = n.split()
    print(int(a) - int(b))
elif '*' in n:
    a, b = n.split()
    print(int(a) * int(b))
else:
    a, b = n.split()
    print(int(a) // int(b))