The next step is also a generalization. Instead of drawing squares, polygon draws regular
polygons with any number of sides. Here is a solution:
def polygon(t, n, length):
angle = 360 / n
for i in range(n):
t.fd(length)
t.lt(angle)
polygon(bob, 7, 70)

polygon(bob, n=7, length=70)

