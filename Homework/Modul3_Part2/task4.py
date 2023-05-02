n = int(input('Введите число: '))
sum_n = n
mx = n
mn = n
while n != 7:
    n = int(input('Введите число: '))
    sum_n += n
    if mx < n:
        mx = n
    if mn > n:
        mn = n
    print ('Summa=', sum_n)
    print ('Max=', mx)
    print ('Min=', mn)
    print ('Good bye!')