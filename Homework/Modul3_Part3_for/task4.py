count1=0
count2=0
for a in range(100,9999):
    n1=(a//1000)
    n2=(a//100)%10
    n3=(a%100)//10
    n4=a%10
    if a <1000:
        (n2!=n3 or n2!=n4 or n3!=n4)
        count1 += 1
    if a >=1000:
        (n1!=n2 or n1!=n3 or n1!=n4 or n2!=n3 or n2!=n4 or n3!=n4)
        count2 += 1
        print("Количество разных целых чисел в диапазоне от 100 до 9999:",count1+count2 )
