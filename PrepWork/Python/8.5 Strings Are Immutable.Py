>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment

The reason for the error is that strings are immutable, which means you can’t change an
existing string. The best you can do is create a new string that is a variation on the original:
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> new_greeting
'Jello, world!'