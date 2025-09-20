import math

def point_circle_position(x,y,r):
    if r <= 0:
        return "Invalid radius"
    d = round(math.sqrt(x*x + y*y), 2)
    if d == r:
        return "On"
    elif d < r:
        return "Inside"
    else:
        return "Outside"