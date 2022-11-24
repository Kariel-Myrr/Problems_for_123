
# Дан прямоугольник заданный угловыми точками - найти его середину

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

print((x2 - x1) / 2 + x1, (y2 - y1) / 2 + y1)