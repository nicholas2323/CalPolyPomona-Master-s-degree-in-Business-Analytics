Exercise 6.1. Draw a stack diagram for the following program. What does the program print?
def b(z):
prod = a(z, z)
print(z, prod)
return prod
def a(x, y):
x = x + 1
return x * y
def c(x, y, z):
total = x + y + z
square = b(total)**2
return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
Exercise 6.2. The Ackermann function, A(m, n), is defined:
A(m, n) =



n + 1 if m = 0
A(m − 1, 1) if m > 0 and n = 0
A(m − 1, A(m, n − 1)) if m > 0 and n > 0.

The following are functions that take a string argument and return the first, last, and middle letters:
def first(word):
return word[0]
def last(word):
return word[-1]
def middle(word):
return word[1:-1]