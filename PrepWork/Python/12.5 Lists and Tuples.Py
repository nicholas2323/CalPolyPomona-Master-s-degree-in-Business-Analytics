This example zips a string and a list:
>>> s = 'abc'
>>> t = [0, 1, 2]
>>> zip(s, t)
<zip object at 0x7f7d0a9e7c48>

For Loop: 
    >>> for pair in zip(s, t):
... print(pair)
...
('a', 0)
('b', 1)
('c', 2)

If you want to use list operators and methods, you can use a zip object to make a list:
>>> list(zip(s, t))
[('a', 0), ('b', 1), ('c', 2)]

If the sequences are not the same length, the result has the length of the shorter one.
>>> list(zip('Anne', 'Elk'))
[('A', 'E'), ('n', 'l'), ('n', 'k')]
You can use tuple assignment in a for loop to traverse a list of tuples:
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
print(number, letter)

If you combine zip, for and tuple assignment, you get a useful idiom for traversing two
(or more) sequences at the same time. For example, has_match takes two sequences, t1
and t2, and returns True if there is an index i such that t1[i] == t2[i]:
def has_match(t1, t2):
for x, y in zip(t1, t2):
if x == y:
return True
return False

If you need to traverse the elements of a sequence and their indices, you can use the built-in
function enumerate:
for index, element in enumerate('abc'):
print(index, element)
The result from enumerate is an enumerate object, which iterates a sequence of pairs; each
pair contains an index (starting from 0) and an element from the given sequence. In this
example, the output is
0 a
1 b
2 c
Again.