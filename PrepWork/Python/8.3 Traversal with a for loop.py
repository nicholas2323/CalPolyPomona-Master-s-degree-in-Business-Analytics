This pattern of processing is called a traversal. One way to write a traversal is with a
while loop:
index = 0
while index < len(fruit):
letter = fruit[index]
print(letter)
index = index + 1

Another way to write a traversal is with a for loop:
for letter in fruit:
print(letter)

In Robert McCloskey’s
book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack,
Ouack, Pack, and Quack. This loop outputs these names in order:
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
print(letter + suffix)
The output is:
Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack