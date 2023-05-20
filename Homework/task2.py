def even_numbers_between (a, b):
    for i in range (a+1, b):
        if i %2 == 0:
            print (i)
even_numbers_between (1, 10)