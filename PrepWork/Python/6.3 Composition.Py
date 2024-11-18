We just wrote a function, distance, that does that:
radius = distance(xc, yc, xp, yp)

The next step is to find the area of a circle with that radius; we just wrote that, too:
result = area(radius)

Encapsulating these steps in a function, we get:
def circle_area(xc, yc, xp, yp):
radius = distance(xc, yc, xp, yp)
result = area(radius)
return result

def circle_area(xc, yc, xp, yp):
return area(distance(xc, yc, xp, yp))