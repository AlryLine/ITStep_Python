def count_primes (numbers):
    count = 0
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range (2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
    return count
print (count_primes([1,2,-4,5,6,3,7,11]))