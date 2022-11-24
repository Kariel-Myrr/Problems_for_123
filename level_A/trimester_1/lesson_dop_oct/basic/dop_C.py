
# Дан прямоугольник заданный угловыми точками. Найти его площадь

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

print((x2 - x1) * (y2 - y1))