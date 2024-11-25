For example, some programs use a flag named verbose to
control the level of detail in the output:
verbose = True
def example1():
if verbose:
print('Running example1')

. The following example is
supposed to keep track of whether the function has been called:
been_called = False
def example2():
been_called = True # WRONG

To reassign a global variable inside a function you have to declare the global variable before
you use it:
    
been_called = False
def example2():
global been_called
been_called = True
The global statement tells the interpreter something like, “In this function, when I say
been_called, I mean the global variable; don’t create a local one.”
Here’s an example that tries to update a global variable:
count = 0
def example3():
count = count + 1 # WRONG


def example3():
global count
count += 1
If a global variable refers to a mutable value, you can modify the value without declaring
the variable:
known = {0:0, 1:1}
def example4():
known[2] = 1
So you can add, remove and replace elements of a global list or dictionary, but if you want
to reassign the variable, you have to declare it:
def example5():
global known
known = dict()
