When an expression contains more than one operator, the order of evaluation depends
on the order of operations. For mathematical operators, Python follows mathematical
convention. The acronym PEMDAS is a useful way to remember the rules:
12 Chapter 2. Variables, expressions and statements
• Parentheses have the highest precedence and can be used to force an expression to
evaluate in the order you want. Since expressions in parentheses are evaluated first,
2 * (3-1) is 4, and (1+1)**(5-2) is 8. You can also use parentheses to make an
expression easier to read, as in (minute * 100) / 60, even if it doesn’t change the
result.
• Exponentiation has the next highest precedence, so 1 + 2**3 is 9, not 27, and 2 *
3**2 is 18, not 36.
• Multiplication and Division have higher precedence than Addition and Subtraction.
So 2*3-1 is 5, not 4, and 6+4/2 is 8, not 5.
• Operators with the same precedence are evaluated from left to right (except exponen-
tiation). So in the expression degrees / 2 * pi, the division happens first and the
result is multiplied by pi. To divide by 2π, you can use parentheses or write degrees
/ 2 / pi.
I don’t work very hard to remember the precedence of operators. If I can’t tell by looking
at the expression, I use parentheses to make it obvious.