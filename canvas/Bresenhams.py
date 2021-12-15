from graphics import *
import time

def BresenhamLine(x1, y1, x2, y2, win, color):

    pixels = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    xk, yk = x1, y1

    if dx == 0:
        for k in range (0, dy):
            if y1 > y2:
                yk -= 1
            else:
                yk += 1
            
            pt = Point(xk, yk)
            pixels.append([xk, yk])
            #print(pt)
            pt.setOutline(color)
            #time.sleep(0.001)
            pt.draw(win)

    else:
        slope = dy/float(dx)
        #print(slope)

        if x1 < x2:
            if slope > 1:
                pk = 2 * dx - dy
                for k in range (0, dy):
                    if y1 > y2:
                        yk -= 1
                    else:
                        yk += 1
                    #print(pk)
                    if pk >= 0:
                        xk = xk + 1
                        pk += 2*(dx - dy)
                    else:
                        pk += 2*dx

                    pt = Point(xk, yk)
                    pixels.append([xk, yk])
                    #print(pt)
                    pt.setOutline(color)
                    #time.sleep(0.001)
                    pt.draw(win)

            elif slope < 1:
                pk = 2 * dy - dx
                for k in range (0, dx):
                    xk += 1
                    #print(pk)
                    if pk >= 0:
                        if y1 > y2:
                            yk = yk - 1
                        else:
                            yk = yk + 1
                        pk += 2*(dy - dx)
                    else:
                        pk += 2*dy

                    pt = Point(xk, yk)
                    pixels.append([xk, yk])
                    #print(pt)
                    pt.setOutline(color)
                    #time.sleep(0.001)
                    pt.draw(win)

        elif x1 > x2:
            if slope > 1:
                pk = 2 * dx - dy
                for k in range (0, dy):
                    if y1 < y2:
                        yk += 1
                    else:
                        yk -= 1
                    #print(pk)
                    if pk >= 0:
                        xk = xk - 1
                        pk += 2*(dx - dy)
                    else:
                        pk += 2*dx

                    pt = Point(xk, yk)
                    pixels.append([xk, yk])
                    #print(pt)
                    pt.setOutline(color)
                    #time.sleep(0.001)
                    pt.draw(win)

            elif slope < 1:
                pk = 2 * dy - dx
                for k in range (0, dx):
                    xk -= 1
                    #print(pk)
                    if pk >= 0:
                        if y1 < y2:
                            yk = yk + 1
                        else:
                            yk = yk - 1
                        pk += 2*(dy - dx)
                    else:
                        pk += 2*dy

                    pt = Point(xk, yk)
                    pixels.append([xk, yk])
                    #print(pt)
                    pt.setOutline(color)
                    #time.sleep(0.001)
                    pt.draw(win)

        elif slope == 0:
            for k in range (0, dx):
                if x1 > x2:
                    xk -= 1
                else:
                    xk += 1
                
                pt = Point(xk, yk)
                pixels.append([xk, yk])
                #print(pt)
                pt.setOutline(color)
                #time.sleep(0.001)
                pt.draw(win)

    return pixels