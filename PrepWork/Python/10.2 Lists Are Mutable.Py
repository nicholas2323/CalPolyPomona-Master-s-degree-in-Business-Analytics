he expression inside the brackets specifies the index.
Remember that the indices start at 0:
>>> cheeses[0]
'Cheddar'
Unlike strings, lists are mutable. When the bracket operator appears on the left side of an
assignment, it identifies the element of the list that will be assigned.
>>> numbers = [42, 123]
>>> numbers[1] = 5
>>> numbers
[42, 5

The in operator also works on lists.
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False