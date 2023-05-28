def multiplication_of_numbers_in_range (num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    res = 1
    for i in range (num1, num2+1):
        res *= i
    return res
print (multiplication_of_numbers_in_range (1, 4))
    