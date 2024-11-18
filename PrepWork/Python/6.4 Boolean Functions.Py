For example:
def is_divisible(x, y):
if x % y == 0:
return True
else:
return False

It is common to give boolean functions names that sound like yes/no questions;
is_divisible returns either True or False to indicate whether x is divisible by y.
Here is an example:
>>> is_divisible(6, 4)
False
>>> is_divisible(6, 3)
True
The result of the == operator is a boolean, so we can write the function more concisely by
returning it directly:
def is_divisible(x, y):
return x % y == 0
Boolean functions are often used in conditional statements:
if is_divisible(x, y):
print('x is divisible by y')
It might be tempting to write something like:
if is_divisible(x, y) == True:
print('x is divisible by y')

