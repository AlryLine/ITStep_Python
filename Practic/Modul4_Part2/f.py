from re import S


def sum_of_el (a):
    if type(a)  == list:
        return sum (a)

def max_of_el (a):
    if type(a)  == list:
        return max (a)

def stars (n):
    if n != 1:
        stars (n - 1)
    print ('*', end = '')

