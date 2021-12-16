from graphics import *

def SetPixel(win, x, y, new_color, pixels):
    pt = Point(x, y)
    pixels[x][y] = 3
    pt.setOutline(new_color)
    pt.draw(win)

def FloodFillalgo(win, x, y, new_color, pixels):
    if pixels[x][y] == 2:
        SetPixel(win, x, y, new_color, pixels)
        FloodFillalgo(win, x+1, y, new_color, pixels)
        FloodFillalgo(win, x-1, y, new_color, pixels)
        FloodFillalgo(win, x, y-1, new_color, pixels)
        FloodFillalgo(win, x, y+1, new_color, pixels)

    return