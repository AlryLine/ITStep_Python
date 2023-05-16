from secrets import choice


print('Добрий день!')
while True:
    sum_uah = int(input('Введіть сумму в гривнях: '))
    sum_usd = sum_uah/2
    print(sum_usd)
    choice = input('Бажаєте ще поміняти гроші (Так або Ні): ')
    if choice == 'Так':
        continue
    if choice == 'Ні':
        break
    



    



