
# Даны две точки - вывести уравнение прямой

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

k = (y2 - y1) / (x2 - x1)

b = y1 - k * x1

print(k, b)