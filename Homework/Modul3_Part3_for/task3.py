count = 0
for i in range (100, 10000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100 % 10
    d = i // 1000
    if a != b and a != c and a != d and b != c and b != d and c != d:
        count += 1
print (count)