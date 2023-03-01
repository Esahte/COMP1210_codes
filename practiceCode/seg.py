from math import sqrt

def segLength(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def sefSlop(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

