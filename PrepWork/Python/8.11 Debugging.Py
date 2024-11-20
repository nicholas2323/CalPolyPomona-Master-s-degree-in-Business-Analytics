def is_reverse(word1, word2):
if len(word1) != len(word2):
return False
i = 0
j = len(word2)
while j > 0:
if word1[i] != word2[j]:
return False
i = i+1

j = j-1
return True


If we test this function with the words “pots” and “stop”, we expect the return value True,
but we get an IndexError:
>>> is_reverse('pots', 'stop')
...
File "reverse.py", line 15, in is_reverse
if word1[i] != word2[j]:
IndexError: string index out of range

For debugging this kind of error, my first move is to print the values of the indices imme-
diately before the line where the error appears.
while j > 0:
print(i, j) # print here
if word1[i] != word2[j]:
return False
i = i+1
j = j-1

Now when I run the program again, I get more information:
>>> is_reverse('pots', 'stop')
0 4

If I fix that error and run the program again, I get:
>>> is_reverse('pots', 'stop')
0 3
1 2
2 1
True