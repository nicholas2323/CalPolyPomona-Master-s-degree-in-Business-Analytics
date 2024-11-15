Conventional division returns a floating-point number: 
>>> minutes = 105
>>> minutes / 60
1.75

But we don’t normally write hours with decimal points. Floor division returns the integer
number of hours, rounding down:
>>> minutes = 105
>>> hours = minutes // 60
>>> hours
1
To get the remainder, you could subtract off one hour in minutes:
>>> remainder = minutes - hours * 60
>>> remainder
45
An alternative is to use the modulus operator, %, which divides two numbers and returns
the remainder.
>>> remainder = minutes % 60
>>> remainder
45

Notes: 
    x % 10 yields the right-most digit of x (in base 10). 
    Similarly x % 100 yields the last two digits.