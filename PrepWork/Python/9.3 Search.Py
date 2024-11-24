The simplest example is:
def has_no_e(word):
for letter in word:
if letter == 'e':
return False
return True

def avoids(word, forbidden):
for letter in word:
if letter in forbidden:
return False
return True

We can return False as soon as we find a forbidden letter; if we get to the end of the loop,
we return True.
uses_only is similar except that the sense of the condition is reversed:
def uses_only(word, available):
for letter in word:
if letter not in available:
return False
return True

uses_all is similar except that we reverse the role of the word and the string of letters:
def uses_all(word, required):
for letter in required:
if letter not in word:
return False
return True

If you were really thinking like a computer scientist, you would have recognized that
uses_all was an instance of a previously solved problem, and you would have written:
def uses_all(word, required):
return uses_only(required, word)
