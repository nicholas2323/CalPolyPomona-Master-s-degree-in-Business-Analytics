def print_twice(bruce):
print(bruce)
print(bruce)

This works with any value that can be printed

>>> print_twice('Spam')
Spam
Spam
>>> print_twice(42)
42
42
>>> print_twice(math.pi)
3.14159265359
3.14159265359

The same rules of composition that apply to built-in functions also apply to programmer-
defined functions, so we can use any kind of expression as an argument for print_twice:
>>> print_twice('Spam '*4)
Spam Spam Spam Spam
Spam Spam Spam Spam
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
The argument is evaluated before the function is called, so in the examples the expressions
'Spam '*4 and math.cos(math.pi) are only evaluated once.
You can also use a variable as an argument:
>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.