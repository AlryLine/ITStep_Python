t = input ('Input text: ')
rw = input ('Input words: ').split (' ')

for w in rw:
    t = t.replace (w, w.upper())
print (t)