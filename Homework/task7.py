def palindrom_number (num):
    n = num
    if str(n) == str(n)[::-1]:
        print("It's palindrom")
    else:
        print("It's not palindrom")

palindrom_number (123321)
palindrom_number (123456)