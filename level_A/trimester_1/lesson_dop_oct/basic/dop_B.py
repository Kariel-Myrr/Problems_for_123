
# Дан прямоугольник заданный угловыми точками. Найти его периметр

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

print(2 * (x1 - x2) + 2 * (y1 - y2))