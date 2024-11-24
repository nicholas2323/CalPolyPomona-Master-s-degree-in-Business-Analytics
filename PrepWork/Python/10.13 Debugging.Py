If you are used to writing string code like this:
word = word.strip()

t = t.sort() # WRONG!

To add an element, you can use the append method or the + operator. Assuming that
t is a list and x is a list element, these are correct:
t.append(x)
t = t + [x]
t += [x]
And these are wrong:
t.append([x]) # WRONG!
t = t.append(x) # WRONG!
t + [x] # WRONG!
t = t + x # WRONG!

Make copies to avoid aliasing.
If you want to use a method like sort that modifies the argument, but you need to
keep the original list as well, you can make a copy.
>>> t = [3, 1, 2]
>>> t2 = t[:]
>>> t2.sort()
>>> t
[3, 1, 2]
>>> t2
[1, 2, 3]
In this example you could also use the built-in function sorted, which returns a new,
sorted list and leaves the original alone.
>>> t2 = sorted(t)
>>> t
[3, 1, 2]
>>> t2
[1, 2, 3]

