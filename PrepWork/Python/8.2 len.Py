]len is a built-in function that returns the number of characters in a string:
    
>>> fruit = 'banana'
>>> len(fruit)
6

To get the last letter of a string, you might be tempted to try something like this:
>>> length = len(fruit)
>>> last = fruit[length]
IndexError: string index out of range

The reason for the IndexError is that there is no letter in ’banana’ with the index 6. Since
we started counting at zero, the six letters are numbered 0 to 5. To get the last character,
you have to subtract 1 from length:
>>> last = fruit[length-1]
>>> last
'a'