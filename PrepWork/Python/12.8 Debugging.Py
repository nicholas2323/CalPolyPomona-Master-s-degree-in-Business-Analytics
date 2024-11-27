Here’s the result for a simple list:
>>> from structshape import structshape
>>> t = [1, 2, 3]
>>> structshape(t)
'list of 3 int'
A fancier program might write “list of 3 ints”, but it was easier not to deal with plurals.
Here’s a list of lists:
>>> t2 = [[1,2], [3,4], [5,6]]
>>> structshape(t2)
'list of 3 list of 2 int'
If the elements of the list are not the same type, structshape groups them, in order, by
type:
>>> t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
>>> structshape(t3)
'list of (3 int, float, 2 str, 2 list of int, int)'
Here’s a list of tuples:
>>> s = 'abc'
>>> lt = list(zip(t, s))
>>> structshape(lt)
'list of 3 tuple of (int, str)'
And here’s a dictionary with 3 items that map integers to strings.
>>> d = dict(lt)
>>> structshape(d)
'dict of 3 int->str'
If you are having trouble keeping track of your data structures, structshape can help.