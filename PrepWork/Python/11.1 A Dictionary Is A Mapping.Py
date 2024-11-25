>>> eng2sp = dict()
>>> eng2sp
{}
The squiggly-brackets, {}, represent an empty dictionary. To add items to the dictionary,
you can use square brackets:
>>> eng2sp['one'] = 'uno'
This line creates an item that maps from the key 'one' to the value 'uno'. If we print the
dictionary again, we see a key-value pair with a colon between the key and value:
>>> eng2sp
{'one': 'uno'}

New Dictionary with Three Items: 
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

But if you print eng2sp, you might be surprised:
>>> eng2sp
{'one': 'uno', 'three': 'tres', 'two': 'dos'}
The order of the key-value pairs might not be the same. If you type the same example
on your computer, you might get a different result. In general, the order of items in a
dictionary is unpredictable.
But that’s not a problem because the elements of a dictionary are never indexed with inte-
ger indices. Instead, you use the keys to look up the corresponding values:
>>> eng2sp['two']
'dos'
The key 'two' always maps to the value 'dos' so the order of the items doesn’t matter.
If the key isn’t in the dictionary, you get an exception:
>>> eng2sp['four']
KeyError: 'four'
The len function works on dictionaries; it returns the number of key-value pairs:
>>> len(eng2sp)
3
The in operator works on dictionaries, too; it tells you whether something appears as a key
in the dictionary (appearing as a value is not good enough).
>>> 'one' in eng2sp
True
>>> 'uno' in eng2sp
False
To see whether something appears as a value in a dictionary, you can use the method
values, which returns a collection of values, and then use the in operator:
>>> vals = eng2sp.values()
>>> 'uno' in vals
True