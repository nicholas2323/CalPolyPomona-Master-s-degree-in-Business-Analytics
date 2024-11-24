For is_abecedarian we have to compare adjacent letters, which is a little tricky with a for
loop:
def is_abecedarian(word):
previous = word[0]
for c in word:
if c < previous:
return False
previous = c
return True
An alternative is to use recursion:
def is_abecedarian(word):
if len(word) <= 1:
return True
if word[0] > word[1]:
return False
return is_abecedarian(word[1:])
Another option is to use a while loop:
def is_abecedarian(word):
i = 0
while i < len(word)-1:
if word[i+1] < word[i]:
return False
i = i+1
return True

Here is a version of is_palindrome (see Exercise 6.3) that uses two indices; one starts at
the beginning and goes up; the other starts at the end and goes down.
def is_palindrome(word):
i = 0
j = len(word)-1
while i<j:
if word[i] != word[j]:
    
    return False
i = i+1
j = j-1
return True

Or we could reduce to a previously solved problem and write:
def is_palindrome(word):
return is_reverse(word, word)
Using is_reverse from Section 8.11.