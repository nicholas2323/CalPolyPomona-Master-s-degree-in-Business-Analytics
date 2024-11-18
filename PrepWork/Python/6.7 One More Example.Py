After factorial, the most common example of a recursively defined mathematical func-
tion is fibonacci, which has the following definition (see http://en.wikipedia.org/
wiki/Fibonacci_number):
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(n) = fibonacci(n − 1) + fibonacci(n − 2)

Translated into Python, it looks like: 
def fibonacci(n):
if n == 0:
return 0
elif n == 1:
return 1
else:
return fibonacci(n-1) + fibonacci(n-2