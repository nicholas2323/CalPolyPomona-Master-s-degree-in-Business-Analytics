A string is a sequence of characters and a list is a sequence of values, but a list of characters
is not the same as a string. To convert from a string to a list of characters, you can use list:
>>> s = 'spam'
>>> t = list(s)
>>> t
['s', 'p', 'a', 'm']

Because list is the name of a built-in function, you should avoid using it as a variable
name. I also avoid l because it looks too much like 1. So that’s why I use t.
The list function breaks a string into individual letters. If you want to break a string into
words, you can use the split method:
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> t
['pining', 'for', 'the', 'fjords']
An optional argument called a delimiter specifies which characters to use as word bound-
aries. The following example uses a hyphen as a delimiter:
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> t = s.split(delimiter)
>>> t
['spam', 'spam', 'spam']
join is the inverse of split. It takes a list of strings and concatenates the elements. join is
a string method, so you have to invoke it on the delimiter and pass the list as a parameter:
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> s = delimiter.join(t)
>>> s
'pining for the fjords'
In this case the delimiter is a space character, so join puts a space between words. To
concatenate strings without spaces, you can use the empty string, '', as a delimiter.