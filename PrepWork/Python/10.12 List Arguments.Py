When you pass a list to a function, the function gets a reference to the list. If the function
modifies the list, the caller sees the change. For example, delete_head removes the first
element from a list:
def delete_head(t):
del t[0]
Here’s how it is used:
>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
>>> letters
['b', 'c']

It is important to distinguish between operations that modify lists and operations that cre-
ate new lists. For example, the append method modifies a list, but the + operator creates a
new list.
Here’s an example using append:
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> t1
[1, 2, 3]
>>> t2
None

The return value from append is None.
Here’s an example using the + operator:
>>> t3 = t1 + [4]
>>> t1
[1, 2, 3]
>>> t3
[1, 2, 3, 4]
The result of the operator is a new list, and the original list is unchanged.

This difference is important when you write functions that are supposed to modify lists.
For example, this function does not delete the head of a list:
def bad_delete_head(t):
t = t[1:] # WRONG!
The slice operator creates a new list and the assignment makes t refer to it, but that doesn’t
affect the caller.
>>> t4 = [1, 2, 3]
>>> bad_delete_head(t4)
>>> t4
[1, 2, 3]
At the beginning of bad_delete_head, t and t4 refer to the same list. At the end, t refers
to a new list, but t4 still refers to the original, unmodified list.
An alternative is to write a function that creates and returns a new list. For example, tail
returns all but the first element of a list:
def tail(t):
return t[1:]
This function leaves the original list unmodified. Here’s how it is used:
>>> letters = ['a', 'b', 'c']
>>> rest = tail(letters)
>>> rest
['b', 'c']