n = int(input('Input number: '))
sum_n = n
mx = n
mn = n
while n != 7:
    n = int(input('Input number: '))
    sum_n += n
    if mx < n:
        mx = n
    elif mn > n:
        mn = n
    print ('Summa=', sum_n)
    print ('Max=', mx)
    print ('Min=', mn)
else:
    n == 7
    print ('Good bye!')