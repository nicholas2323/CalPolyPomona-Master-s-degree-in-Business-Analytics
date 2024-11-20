The relational operators work on strings. To see if two strings are equal:
if word == 'banana':
print('All right, bananas.')
Other relational operations are useful for putting words in alphabetical order:
if word < 'banana':
print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
print('Your word, ' + word + ', comes after banana.')
else:
print('All right, bananas.')