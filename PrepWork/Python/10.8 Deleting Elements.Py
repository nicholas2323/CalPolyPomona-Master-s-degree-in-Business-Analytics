There are several ways to delete elements from a list. If you know the index of the element
you want, you can use pop:
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> t
['a', 'c']
>>> x
'b'
pop modifies the list and returns the element that was removed. If you don’t provide an
index, it deletes and returns the last element.
If you don’t need the removed value, you can use the del operator:
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> t
['a', 'c']
If you know the element you want to remove (but not the index), you can use remove:
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> t
['a', 'c']
The return value from remove is None.
To remove more than one element, you can use del with a slice index:
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> t
['a', 'f']
As usual, the slice selects all the elements up to but not including the second index