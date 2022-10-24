
# Дан прямоугольник заданный центральной точкой и его шириной и высотой.
# Вывести угловые точки.

x, y = [int(i) for i in input().split()]
w, h = [int(i) for i in input().split()]

print( x - w/2, y - h/2)
print( x + w/2, y + h/2)