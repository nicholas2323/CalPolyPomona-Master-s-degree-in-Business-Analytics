Dictionaries have a method called items that returns a sequence of tuples, where each
tuple is a key-value pair.
>>> d = {'a':0, 'b':1, 'c':2}
>>> t = d.items()
>>> t
dict_items([('c', 2), ('a', 0), ('b', 1)])
The result is a dict_items object, which is an iterator that iterates the key-value pairs. You
can use it in a for loop like this:
>>> for key, value in d.items():
... print(key, value)
...
c 2
a 0
b 1
As you should expect from a dictionary, the items are in no particular order.
Going in the other direction, you can use a list of tuples to initialize a new dictionary:
>>> t = [('a', 0), ('c', 2), ('b', 1)]
>>> d = dict(t)
>>> d
{'a': 0, 'c': 2, 'b': 1}
Combining dict with zip yields a concise way to create a dictionary:
>>> d = dict(zip('abc', range(3)))
>>> d
{'a': 0, 'c': 2, 'b': 1}
The dictionary method update also takes a list of tuples and adds them, as key-value pairs,
to an existing dictionary.
It is common to use tuples as keys in dictionaries (primarily because you can’t use lists). For
example, a telephone directory might map from last-name, first-name pairs to telephone
numbers. Assuming that we have defined last, first and number, we could write:
directory[last, first] = number
The expression in brackets is a tuple. We could use tuple assignment to traverse this dic-
tionary.
for last, first in directory:
print(first, last, directory[last,first])