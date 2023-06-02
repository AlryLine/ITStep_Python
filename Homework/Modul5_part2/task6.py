def pow_of_elements (p,numbers):
    pow_of_num_lst = []
    for n in numbers:
        pow_of_num_lst.append(n ** p)
    return pow_of_num_lst
print (pow_of_elements(3,[2,3,4]))