print('Добрий день!')
a=int(input('Введіть число: '))
b=int(input('Введіть число: '))
print('Варіанти')
print('1: сумма')
print('2: різниця')
print('3: добуток')
choice = int(input('Ваш вибір: '))
if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
else:
    print('Введіть коректне число')

