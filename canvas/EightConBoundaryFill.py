from graphics import *

def SetPixel(win, x, y, color, pixels):
    pt = Point(x, y)
    pixels[x][y] = 2
    pt.setOutline(color)
    pt.draw(win)

def BoundFill(win, x, y, color, pixels):
    if pixels[x][y] != 1 and pixels[x][y] != 2:
        SetPixel(win, x, y, color, pixels)

        x, y = BoundFill(win, x+1, y, color, pixels)
        x, y = BoundFill(win, x, y+1, color, pixels)
        x, y = BoundFill(win, x-1, y, color, pixels)
        x, y = BoundFill(win, x, y-1, color, pixels)
        x, y = BoundFill(win, x-1, y-1, color, pixels)
        x, y = BoundFill(win, x-1, y+1, color, pixels)
        x, y = BoundFill(win, x+1, y-1, color, pixels)
        x, y = BoundFill(win, x+1, y+1, color, pixels)

    return ([x, y])