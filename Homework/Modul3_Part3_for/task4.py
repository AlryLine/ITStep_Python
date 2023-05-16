n = int(input ('Input a number: '))
raz = n
count = 0
rezult = 0
while raz:
    count += 1 
    raz//= 10
raz = n
i = 0
while count:
    number = raz%10
    raz//= 10
    if not (number ==3 or number ==6):
        rezult = rezult + (number * 10 ** i)
        i += 1
    count -= 1
print('Rezult =', rezult)