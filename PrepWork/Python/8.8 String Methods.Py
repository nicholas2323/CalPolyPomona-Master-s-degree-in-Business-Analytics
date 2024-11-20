Instead of the function syntax upper(word), it uses the method syntax word.upper().
>>> word = 'banana'
>>> new_word = word.upper()
>>> new_word
'BANANA'

As it turns out, there is a string method named find that is remarkably similar to the
function we wrote:
>>> word = 'banana'
>>> index = word.find('a')
>>> index
1

Actually, the find method is more general than our function; it can find substrings, not just
characters:
>>> word.find('na')
2
By default, find starts at the beginning of the string, but it can take a second argument, the
index where it should start:
>>> word.find('na', 3)
4
This is an example of an optional argument; find can also take a third argument, the index
where it should stop:
>>> name = 'bob'
>>> name.find('b', 1, 2)
-1