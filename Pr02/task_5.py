from secrets import choice


print('Добрий день!')
a=int(input('Введіть число: '))
b=int(input('Введіть число: '))
print('Будь ласка, зробіть вибір: ')
print('1: сумма')
print('2: різниця')
print('3: добуток')
if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
else:
    print('Введіть коректне число')

