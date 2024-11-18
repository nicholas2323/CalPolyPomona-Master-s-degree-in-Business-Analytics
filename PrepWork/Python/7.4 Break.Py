For example, suppose you want to take input from the user until they type done. You could
write:
while True:
line = input('> ')
if line == 'done':
break
print(line)
print('Done!')

Each time through, it prompts the user with an angle bracket. If the user types done, the
break statement exits the loop. Otherwise the program echoes whatever the user types and
goes back to the top of the loop. Here’s a sample run:
> not done
not done
> done
Done!