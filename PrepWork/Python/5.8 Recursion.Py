 For example, look at the following function:
def countdown(n):
if n <= 0:
print('Blastoff!')
else:
print(n)
countdown(n-1)

What happens if we call this function like this?
>>> countdown(3)

And then you’re back in __main__. So, the total output looks like this:
3
2
1
Blastoff!

As another example, we can write a function that prints a string n times.
def print_n(s, n):
if n <= 0:
return
print(s)
print_n(s, n-1)