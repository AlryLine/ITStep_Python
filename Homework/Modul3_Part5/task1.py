print ('Вітаю! :)')
print ('Маю для Вас цікавенькі малюнки! Будь-ласка, виберіть варіант від 1 до 5!')
print ('Варіанти: ')
print ('1: а')
print ('2: б')
print ('3: в')
print ('4: г')
print ('5: д')

choice = int(input('Ваш вибір: '))
if choice == 1:
    n = 10
    for i in range (n):
        print (' '*i, '*'*(n - i), sep= ' ')
elif choice == 2:
    n = 10
    for i in range (n):
        print ('*'*(i + 1), ' '*(n - i), sep= ' ')
elif choice == 3:
    n = 10
    for i in range (n):
        print (' '*i, (n-2*i)*'*', ' '*i, sep= ' ')
elif choice == 4:
    n = 5
    for i in range (- 5, 6):
        print (' '*(n - i), (2*i)*'*', ' '*(n - i), sep= ' ')
elif choice == 5:
    n = 10
    for i in range (n//2):
        print (' '*i, (n-2*i)*'*', ' '*i, sep= ' ')
    for i in range (n//3, -1, -1):
        print (' '*i, (n-2*i)*'*', ' '*i, sep= ' ')
else:
    print ('Будь-ласка, введіть коректне число від 1 до 5!')
print ('До зустрічі! :)')