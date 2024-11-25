Here is a function that inverts a dictionary:
def invert_dict(d):
inverse = dict()
for key in d:
val = d[key]
if val not in inverse:
inverse[val] = [key]
else:
inverse[val].append(key)
return inverse

Each time through the loop, key gets a key from d and val gets the corresponding value.
If val is not in inverse, that means we haven’t seen it before, so we create a new item and
initialize it with a singleton (a list that contains a single element). Otherwise we have seen
this value before, so we append the corresponding key to the list.
Here is an example:
>>> hist = histogram('parrot')
>>> hist
{'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
>>> inverse = invert_dict(hist)
>>> inverse
{1: ['a', 'p', 't', 'o'], 2: ['r']}
Figure 11.1 is a state diagram showing hist and inverse. A dictionary is represented as a
box with the type dict above it and the key-value pairs inside. If the values are integers,
floats or strings, I draw them inside the box, but I usually draw lists outside the box, just
to keep the diagram simple.
Lists can be values in a dictionary, as this example shows, but they cannot be keys. Here’s
what happens if you try:
>>> t = [1, 2, 3]
>>> d = dict()
>>> d[t] = 'oops'
Traceback (most recent call last):
File "<stdin>", line 1, in ?
TypeError: list objects are unhashable
I mentioned earlier that a dictionary is implemented using a hashtable and that means that
the keys have to be hashable.