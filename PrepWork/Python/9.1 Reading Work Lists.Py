>>> fin = open('words.txt')

>>> fin.readline()
'aa\n'

>>> fin.readline()
'aah\n'

Or, if it’s the newline character that’s bothering you, we can get rid of it with the
string method strip:
>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'

You can also use a file object as part of a for loop. This program reads words.txt and
prints each word, one per line:
fin = open('words.txt')
for line in fin:
word = line.strip()
print(word)