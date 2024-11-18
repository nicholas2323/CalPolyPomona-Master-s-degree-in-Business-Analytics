What happens if we call factorial and give it 1.5 as an argument?
>>> factorial(1.5)
RuntimeError: Maximum recursion depth exceeded

We can use the built-in function isinstance to verify the type of the argument. While
we’re at it, we can also make sure the argument is positive:
def factorial(n):
if not isinstance(n, int):
print('Factorial is only defined for integers.')
return None
elif n < 0:
print('Factorial is not defined for negative integers.')
return None
elif n == 0:
return 1
else:
return n * factorial(n-1)

In both
cases, the program prints an error message and returns None to indicate that something
went wrong:
>>> print(factorial('fred'))
Factorial is only defined for integers.
None
>>> print(factorial(-2))
Factorial is not defined for negative integers.
None