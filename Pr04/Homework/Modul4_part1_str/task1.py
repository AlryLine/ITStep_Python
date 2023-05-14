text = input ('Input text: ')
text = text.lower ()
text = text.replace (' ', '')
if text != text [::-1]:
    print ('Не паліндром')
else:
    print ('Паліндром')