A segment of a string is called a slice. Selecting a slice is similar to selecting a character:
>>> s = 'Monty Python'
>>> s[0:5]
'Monty'
>>> s[6:12]
'Python'

If you omit the first index (before the colon), the slice starts at the beginning of the string.
If you omit the second index, the slice goes to the end of the string:
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
If the first index is greater than or equal to the second the result is an empty string, repre-
sented by two quotation marks:
>>> fruit = 'banana'
>>> fruit[3:3]
''