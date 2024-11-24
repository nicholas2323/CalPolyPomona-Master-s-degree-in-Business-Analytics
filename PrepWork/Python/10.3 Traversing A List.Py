The most common way to traverse the elements of a list is with a for loop. The syntax is
the same as for strings:
for cheese in cheeses:
print(cheese)

A for loop over an empty list never runs the body:
for x in []:
print('This never happens.')
Although a list can contain another list, the nested list still counts as a single element. The
length of this list is four:
['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]