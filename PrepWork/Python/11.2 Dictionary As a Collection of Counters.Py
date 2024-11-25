Here is what the code might look like:
def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
else:
d[c] += 1
return d

Here’s how it works:
>>> h = histogram('brontosaurus')
>>> h
{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
The histogram indicates that the letters 'a' and 'b' appear once; 'o' appears twice, and
so on.
Dictionaries have a method called get that takes a key and a default value. If the key
appears in the dictionary, get returns the corresponding value; otherwise it returns the
default value. For example:
>>> h = histogram('a')
>>> h
{'a': 1}
>>> h.get('a', 0)

1
>>> h.get('c', 0)
0
As an exercise, use get to write histogram more concisely. You should be able to eliminate
the if statement.
