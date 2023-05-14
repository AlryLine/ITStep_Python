text = input ('Input text: ')
reserved_words = input ('Input words: ').split (' ')

for word in reserved_words:
    text = text.replace (word, word.upper())
print (text)