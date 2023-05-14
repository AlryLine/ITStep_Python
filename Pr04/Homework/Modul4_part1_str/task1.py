s = input ()
s = s.lower ()
s = s.replace (' ', '')
if s != s [::-1]:
    print ('Не паліндром')
else:
    print ('Паліндром')