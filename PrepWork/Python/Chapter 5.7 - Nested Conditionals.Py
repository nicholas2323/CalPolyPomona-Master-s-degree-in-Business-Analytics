if x == y:
print('x and y are equal')
else:
if x < y:
print('x is less than y')
else:
print('x is greater than y')

For example, we can rewrite the following code using a single conditional:
if 0 < x:
if x < 10:
print('x is a positive single-digit number.')

The print statement runs only if we make it past both conditionals, so we can get the same
effect with the and operator:
if 0 < x and x < 10:
print('x is a positive single-digit number.')

For this kind of condition, Python provides a more concise option:
if 0 < x < 10:
print('x is a positive single-digit number.')