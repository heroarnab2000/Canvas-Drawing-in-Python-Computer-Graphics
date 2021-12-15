from graphics import *
import time

def MidpointEllipse(win, rx, ry, xc, yc):

    x = 0
    y = ry

    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while (dx < dy):

        pt1 = Point(x + xc, y + yc)
        pt2 = Point(-x + xc, y + yc)
        pt3 = Point(x + xc, -y + yc)
        pt4 = Point(-x + xc, -y + yc)

        pt1.setOutline('blue')
        pt2.setOutline('blue')
        pt3.setOutline('blue')
        pt4.setOutline('blue')

        pt1.draw(win)
        pt2.draw(win)
        pt3.draw(win)
        pt4.draw(win)

        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

        time.sleep(0.001)

    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry))

    while (y >= 0):

        pt5 = Point(x + xc, y + yc)
        pt6 = Point(-x + xc, y + yc)
        pt7 = Point(x + xc, -y + yc)
        pt8 = Point(-x + xc, -y + yc)

        pt5.draw(win)
        pt6.draw(win)
        pt7.draw(win)
        pt8.draw(win)

        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)