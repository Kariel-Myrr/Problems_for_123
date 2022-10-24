
# Найти длину диагоналей

import math

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)