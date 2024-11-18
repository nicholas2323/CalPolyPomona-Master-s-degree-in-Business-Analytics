e = math.exp(1.0)
height = radius * math.sin(radians)

The first example is area,
which returns the area of a circle with the given radius:
def area(radius):
a = math.pi * radius**2
return a

The expression can be arbitrarily
complicated, so we could have written this function more concisely:
def area(radius):
return math.pi * radius**2

Multiple Return Statements, one in each branch of a conditional: 
def absolute_value(x):
if x < 0:
return -x
else:
return x

In a fruitful function, it is a good idea to ensure that every possible path through the pro-
gram hits a return statement. For example:
def absolute_value(x):
if x < 0:
return -x
if x > 0:
return 

As an exercise, write a compare function that takes two values, x and y, and returns 1 if x
> y, 0 if x == y, and -1 if x < y.