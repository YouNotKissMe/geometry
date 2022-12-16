

def number3(a1, a2, b1, b2, c1, c2):
    if ((c1 - a1) * (b1 - a1) + (c2 - a2) * (b2 - a2)) * ((c1 - b1) * (a1 - b1) + (c2 - b2) * (a2 - b2)) >= 0:
        print('Перпиндикуляр попадает на отрезок')
    else:
        print('Перпиндикуляр попадает на продолжение отрезка')


def number4(a, b, x1, y1, x2, y2):
    if (a * x1 - y1 + b) * (a * x2 - y2 + b) <= 0:
        print('Прямая и отрезок пересикаются')
    else:
        print('Прямая и отрезок не пересикаются')


def number5(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3) * (x4 - x3) * (y2 - y3) - (y4 - y3) * (x2 - x3) <= 0 and \
            (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) * (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1) <= 0:
        print('Отрезки пересикаются')
    else:
        print('Отрезки не пересикаются')


def number6(x1, y1, x2, y2, x3, y3, x4, y4):
    a = (x1 - x4) * (y2 - y1) - (x2 - x1) * (y1 - y4)
    b = (x2 - x4) * (y3 - y2) - (x3 - x2) * (y2 - y4)
    c = (x3 - x4) * (y1 - y3) - (x1 - x3) * (y3 - y4)
    if a == 0 or b > 0 or c < 0:
        print('Точка лежит на стороне треугольника')
    elif a == 0 or b < 0 or c < 0:
        print('Точка лежит на продолжении треугольника')
    elif a == 0 or b > 0 or c > 0:
        print('Точка лежит на продолжении треугольника')
    elif a == 0 or b == 0 or c > 0:
        print('Точка лежит на вершине треугольника')
    elif ((a > 0) and b > 0 and c > 0) or (a < 0 and b < 0 and c < 0):
        print('Точка лежит внутри треугольника')
    else:
        print('Точка лежит на вне треугольника')


# ot3 = [float(i) for i in input('Введите координаты  отрезка').split()]
# z = [float(i) for i in input('Введите координаты точки z:').split()]
# number3(*ot3, *z)
# y = float(input('Введите y:'))
# a = float(input('Введите a:'))
# x = float(input('Введите x:'))
# b = float(input('Введите b:'))
# x1 = float(input('Введите x1:'))
# x2 = float(input('Введите x2:'))
# y1 = float(input('Введите y1:'))
# y2 = float(input('Введите y2:'))
# number4(a, b, x1, y1, x2, y2)
# ot1 = [float(i) for i in input('Введите координаты 1 отрезка').split()]
# ot2 = [float(i) for i in input('Введите координаты 2 отрезка').split()]
# number5(*ot1, *ot2)
triangle = [float(i) for i in input('Введите координаты треугольника').split()]
dot = [float(i) for i in input('Введите координаты точки').split()]
number6(*triangle, *dot)
