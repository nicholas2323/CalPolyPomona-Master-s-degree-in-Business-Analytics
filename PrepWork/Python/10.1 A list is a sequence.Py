There are several ways to create a new list; the simplest is to enclose the elements in square
brackets ([ and ]):
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit'

The following list contains a string, a float, an
integer, and (lo!) another list:
['spam', 2.0, 5, [10, 20]

A list within another list is nested.
A list that contains no elements is called an empty list; you can create one with empty
brackets, [].
As you might expect, you can assign list values to variables:
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [42, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [42, 123] []