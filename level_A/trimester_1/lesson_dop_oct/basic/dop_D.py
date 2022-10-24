
# Дан прямоугольник заданный угловыми точками - найти его середину

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

print((x1 - x2) / 2 + x1, (y1 - y2) / 2 + y1)