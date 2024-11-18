Factorial Functional, Denoted with symbol !
0! = 1
n! = n(n − 1)!


def factorial(n):
    
If the argument happens to be 0, all we have to do is return 1:
def factorial(n):
if n == 0:
return 1

Otherwise, and this is the interesting part, we have to make a recursive call to find the
factorial of n − 1 and then multiply it by n:
def factorial(n):
if n == 0:
return 1
else:
recurse = factorial(n-1)
result = n * recurse
return result

