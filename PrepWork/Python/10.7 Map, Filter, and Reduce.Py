To add up all the numbers in a list, you can use a loop like this:
def add_all(t):
total = 0
for x in t:
total += x
return total
total is initialized to 0. Each time through the loop, x gets one element from the list.
The += operator provides a short way to update a variable. This augmented assignment
statement,
total += x
is equivalent to
total = total + x

As the loop runs, total accumulates the sum of the elements; a variable used this way is
sometimes called an accumulator.
Adding up the elements of a list is such a common operation that Python provides it as a
built-in function, sum:
>>> t = [1, 2, 3]
>>> sum(t)
6
An operation like this that combines a sequence of elements into a single value is some-
times called reduce

For example, the following
function takes a list of strings and returns a new list that contains capitalized strings:
def capitalize_all(t):
res = []
for s in t:
res.append(s.capitalize())
return res

For example, the following function takes a list of strings and returns a list that contains
only the uppercase strings:
def only_upper(t):
res = []
for s in t:
if s.isupper():
res.append(s)
return res
isupper is a string method that returns True if the string contains only upper case letters.

An operation like only_upper is called a filter because it selects some of the elements and
filters out the others.
Most common list operations can be expressed as a combination of map, filter and reduce.