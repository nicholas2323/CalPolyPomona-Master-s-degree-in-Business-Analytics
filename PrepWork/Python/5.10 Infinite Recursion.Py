Here is a minimal program with an infinite recursion:
 
def recurse():
recurse()

n most programming environments, a program with infinite recursion does not really run
forever. Python reports an error message when the maximum recursion depth is reached:
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
.
.
.
File "<stdin>", line 2, in recurse