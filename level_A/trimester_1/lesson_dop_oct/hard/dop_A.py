import math


def dist(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)


x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

print(dist(x1, y1, x2, y2))
