def dist(x_1, y_1, x_2, y_2) :
    return math.sqrt( (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 )

x, y = [int(i) for i in input().split()]
x1, y1, r = [int(i) for i in input().split()]

if dist(x, y, x1, y1) <= r :
    print("YES")
else:
    print("NO")
