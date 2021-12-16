from graphics import *

def DDAalgo(win, x1, y1, x2, y2):
    
    dy = y2 - y1
    dx = x2 - x1

    if abs(dx) > abs(dy):
        len = dx
    else:
        len = dy

    xinc = dx / float(len)
    yinc = dy / float(len)

    pt = Point(x1, y1)
    pt.setOutline('blue')
    pt.draw(win)

    for i in range(int(len)):
        x1 = x1 + xinc
        y1 = y1 + yinc
        pt = Point(int(x1), int(y1))
        pt.setOutline('blue')
        print(pt)
        print(' ')
        pt.draw(win)