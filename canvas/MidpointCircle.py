from graphics import *
import math

def MidpointCircleAlgo(win, x1, y1, rx, ry):

    radius = int(math.sqrt((x1-rx)**2 + (y1-ry)**2))
    print("The radius of the circle is ", radius, " units\n")

    xr, yr = rx, abs((radius - abs(ry)))

    x0, y0, xk, yk, i = xr, yr, 0, radius, 0

    Pk = (5/4 - radius)
    check = 1
    xcheck = 0

    while yk <= (int(radius*0.25) + radius):
        if Pk < 0:
            xk += 1
            xr += 1
            Pk += 2*(xk) + 1
        else:
            xk += 1
            yk += 1
            xr += 1
            yr += 1
            i += 2
            Pk += 2*(xk) + 1 - 2*(yk)

        check += 2
        if yk >= (int(radius*0.15) + radius) and check % 3 == 0:
            xr -= 1
            xcheck += 1

        time.sleep(0.001)

        pt1 = Point(xr, yr)
        
        pt2 = Point(2*x0-xr, yr-i+2*radius)

        pt3 = Point(2*x0-xr, yr)

        pt4 = Point(xr, yr-i+2*radius)

        pt5 = Point(x0+yk -2*radius+xcheck, y0-xk+ radius)

        pt6 = Point(x0+yk -i-xcheck, y0+xk +radius)

        pt7 = Point(x0+yk -2*radius+xcheck, y0+xk+ radius)

        pt8 = Point(x0+yk -i-xcheck, y0-xk+ radius)

        pt1.setOutline('blue')
        pt2.setOutline('blue')
        pt3.setOutline('blue')
        pt4.setOutline('blue')

        pt5.setOutline('blue')
        pt6.setOutline('blue')
        pt7.setOutline('blue')
        pt8.setOutline('blue')

        pt1.draw(win)
        pt2.draw(win)
        pt3.draw(win)
        pt4.draw(win)
        pt5.draw(win)
        pt6.draw(win)
        pt7.draw(win)
        pt8.draw(win)