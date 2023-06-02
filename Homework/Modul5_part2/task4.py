def count_of_del_numbers (n,numbers):
    len_of_list = len(numbers)
    while True:
        if numbers.count(n) == 0:
            break
        numbers.remove(n)
    return len_of_list - len(numbers)
print(count_of_del_numbers(5,[1,2,3,4,5,6,7,4,5,6,5]))             