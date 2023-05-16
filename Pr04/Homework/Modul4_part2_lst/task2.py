n = input('Введіть арифметичний вираз: ')
lst_n = []
lst_op = ['+', '-', '*', '//']

for n in lst_n:
    lst_n.insert ( lst_op )

if '+' in lst_op:
    a, b = lst_op.split ('+')
    print (int(a) + int(b))