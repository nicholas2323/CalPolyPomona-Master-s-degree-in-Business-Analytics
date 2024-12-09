9.5 Debugging
Testing programs is hard. The functions in this chapter are relatively easy to test because
you can check the results by hand. Even so, it is somewhere between difficult and impos-
sible to choose a set of words that test for all possible errors.
Taking has_no_e as an example, there are two obvious cases to check: words that have an
‘e’ should return False, and words that don’t should return True. You should have no
trouble coming up with one of each.
Within each case, there are some less obvious subcases. Among the words that have an
“e”, you should test words with an “e” at the beginning, the end, and somewhere in the
middle. You should test long words, short words, and very short words, like the empty
string. The empty string is an example of a special case, which is one of the non-obvious
cases where errors often lurk.
In addition to the test cases you generate, you can also test your program with a word list
like words.txt. By scanning the output, you might be able to catch errors, but be careful:
you might catch one kind of error (words that should not be included, but are) and not
another (words that should be included, but aren’t).
In general, testing can help you find bugs, but it is not easy to generate a good set of
test cases, and even if you do, you can’t be sure your program is correct. According to a
legendary computer scientist:
Program testing can be used to show the presence of bugs, but never to show
their absence!
— Edsger W. Dijkstra