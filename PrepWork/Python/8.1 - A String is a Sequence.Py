A string is a sequence of characters. You can access the characters one at a time with the
bracket operator:
>>> fruit = 'banana'
>>> letter = fruit[1]

The expression in brackets is called an index. The index indicates which character in the
sequence you want (hence the name).
But you might not get what you expect:
>>> letter
'a'

>>> letter = fruit[0]
>>> letter
'b'
So b is the 0th letter (“zero-eth”) of 'banana', a is the 1th letter (“one-eth”), and n is the 2th
letter (“two-eth”).
As an index you can use an expression that contains variables and operators:
>>> i = 1
>>> fruit[i]
'a'
>>> fruit[i+1]
'n'

But the value of the index has to be an integer. Otherwise you get:
>>> letter = fruit[1.5]
TypeError: string indices must be integers