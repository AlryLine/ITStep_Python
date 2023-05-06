count = 0
for i in range (100, 10000):
    a = i // 1000
    b = i // 100 % 10
    c = i // 10 % 10
    d = i % 10
    if a != b or a != c or a != d or b != c or b != d or c != d:
        count += 1
    print (count)