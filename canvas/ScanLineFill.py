from graphics import *

def Intersection(x1, y1, x2, y2, LE, RE):

    if y1 > y2:
        
        temp = x1
        x1 = int(x2)
        x2 = int(temp)

        temp = y1
        y1 = int(y2)
        y2 = int(temp)

    if y2 == y1: slope_inv = x2 - x1
    else: slope_inv = (x2 - x1) / (y2 - y1)

    x = x1

    for y in range (y1, y2):

        if LE[y] > x: LE[y] = int(x)
        if RE[y] < x: RE[y] = int(x)

        x += slope_inv

def ScanLineFill(win, p, LE, RE, n, in_y, fin_y, color):

    pixels = []
    for i in range (0, n-1):
        Intersection(int(p[i].x)+1, int(p[i].y), int(p[i+1].x), int(p[i+1].y), LE, RE)
    Intersection(int(p[0].x)+1, int(p[0].y), int(p[n-1].x), int(p[n-1].y), LE, RE)
    
    for y in range (int(in_y), int(fin_y)):
        for x in range (LE[y], RE[y]):
            pt = Point(x,y)
            pixels.append([x, y])
            pt.setOutline(color)
            pt.draw(win)

    return pixels