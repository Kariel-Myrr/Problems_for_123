
# Дана точка и прямоугольник. Сказать является ли точка в прямоугольнике

x, y = [int(i) for i in input().split()]
x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

if x1 <= x and x <= x2 and y1 <= y and y <= y2:
    print("YES")
else:
    print("NO")