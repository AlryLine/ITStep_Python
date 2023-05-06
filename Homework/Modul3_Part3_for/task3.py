count = 0
for i in range (100, 10000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100 % 10
    d = i // 1000
    if a != b or a != c or a != d or b != c or b != d or c != d:
        count += 1
print (count)