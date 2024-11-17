In Python 2, the same function is called
raw_input.
>>> text = input()
What are you waiting for?
>>> text
'What are you waiting for?'

efore getting input from the user, it is a good idea to print a prompt telling the user what
to type. input can take a prompt as an argument:
>>> name = input('What...is your name?\n')
What...is your name?
Arthur, King of the Britons!
>>> name
'Arthur, King of the Britons!'

If you expect the user to type an integer, you can try to convert the return value to int:
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
42
>>> int(speed)
42

But if the user types something other than a string of digits, you get an error:
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10