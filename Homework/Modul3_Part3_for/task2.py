count = 0
for i in range (100, 1000):
    a = i // 100 % 10
    b = i // 10 % 10
    c = i % 10
    if a == b or a == c or b == c:
        count += 1
    print (count)