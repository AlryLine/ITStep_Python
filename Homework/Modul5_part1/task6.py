def count_of_digit_in_number (n):
    count = 0
    if n == 0:
        return 1
    elif n < 0:
        n *= -1
    while n > 0:
        n //= 10
        count += 1
    return count
print (count_of_digit_in_number (234567))