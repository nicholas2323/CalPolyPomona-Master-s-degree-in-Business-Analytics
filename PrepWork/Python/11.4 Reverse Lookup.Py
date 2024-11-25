Depending on the application, you might
be able to pick one, or you might have to make a list that contains all of them. Second,
there is no simple syntax to do a reverse lookup; you have to search.
Here is a function that takes a value and returns the first key that maps to that value:
def reverse_lookup(d, v):
for k in d:
if d[k] == v:
return k
raise LookupError()

If we get to the end of the loop, that means v doesn’t appear in the dictionary as a value, so
we raise an exception.
Here is an example of a successful reverse lookup:
>>> h = histogram('parrot')
>>> key = reverse_lookup(h, 2)
>>> key
'r'

And an unsuccessful one:
>>> key = reverse_lookup(h, 3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 5, in reverse_lookup
LookupError

When you raise an exception, you can provide a detailed error message as an optional
argument. For example:
>>> raise LookupError('value does not appear in the dictionary')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
LookupError: value does not appear in the dictionary
