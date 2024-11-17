>>> import time
>>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours, minutes, and
seconds, plus the number of days since the epoch.

Exercise 5.4. What is the output of the following program? Draw a stack diagram that shows the
state of the program when it prints the result.
def recurse(n, s):
if n == 0:
print(s)
else:
recurse(n-1, n+s)
recurse(3, 0)

def draw(t, length, n):
if n == 0:
return
angle = 50
t.fd(length*n)
t.lt(angle)
draw(t, length, n-1)
t.rt(2*angle)
draw(t, length, n-1)
t.lt(angle)
t.bk(length*n)