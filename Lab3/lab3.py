from math import fabs



class Point:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]


def cross_product(a, b, c):
    return (a.x - b.x) * (b.y - c.y) - (a.y - b.y) * (b.x - c.x)


def square(arr):
    x = [arr[i] for i in range(0,len(arr),2)]
    y = [arr[i] for i in range(1,len(arr), 2)]
    print(x,y)
    res = 0
    for i in range(len(x)):
        if i +1 < len(x):
            res += (x[i]*y[i+1] - x[i+1]*y[i])
    res += (x[-1]*y[0] - x[0]*y[-1])
    return fabs(res/2)


def checkN(x1, y1, x2, y2, x3, y3):
    if ((x2 - x1) * (y3 - y1) -
            (x3 - x1) * (y2 - y1) < 0):
        return True
    else:
        return False


def check(a):
    if q is False:
        print('Многоугольник не простой')
    else:
        print('Многоугольник простой')


case = int(input('Введите задание:'))
dots = [int(x) for x in input('Введите через пробел точки: ').split()]
if case == 1:
    i = 0
    while i < len(dots):
        q = checkN(dots[i], dots[i + 1], dots[i + 2], dots[i + 3], dots[i + 4], dots[i + 5])
        i += 6
        if i == len(dots):
            q = checkN(dots[i - 3], dots[i - 2], dots[i - 1], dots[i], dots[0], dots[1])
            check(q)
        if q is False:
            print('Многоугольник не простой')
            break
if case == 2:
    print(square(dots))
if case == 3:
    points = []
    z = []
    for i in dots:
        if len(z) != 2:
            z.append(i)
        else:

            points.append(z)
            z = []
    points.append(points[1])
    flag = True
    for i in range(len(points) - 2):
        a, b, c = points[i:i + 3]
        tmp = cross_product(Point(a), Point(b), Point(c))
        print(tmp)
        pass
    print(flag)
