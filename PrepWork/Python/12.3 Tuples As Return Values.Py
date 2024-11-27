The built-in function divmod takes two arguments and returns a tuple of two values, the
quotient and remainder. You can store the result as a tuple:
>>> t = divmod(7, 3)
>>> t
(2, 1)
Or use tuple assignment to store the elements separately:
>>> quot, rem = divmod(7, 3)
>>> quot
2
>>> rem
1
Here is an example of a function that returns a tuple:
def min_max(t):
return min(t), max(t)
max and min are built-in functions that find the largest and smallest elements of a sequence.
min_max computes both and returns a tuple of two values.