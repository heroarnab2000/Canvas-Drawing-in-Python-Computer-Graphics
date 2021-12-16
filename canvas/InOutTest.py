from graphics import *

def checkinout(p, pixels):
    count, temp = 0, -1
    for each in pixels:
        if each[1] == p[1] and each[0] < p[0]:
            if abs(each[0] - temp) > 1: count += 1
            temp = each[0]
    print(count)
    if count % 2 == 0: return 'OUTSIDE'
    else: return 'INSIDE'