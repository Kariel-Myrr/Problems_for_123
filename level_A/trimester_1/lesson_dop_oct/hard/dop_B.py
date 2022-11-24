a_x1, a_y1 = [int(i) for i in input().split()]
a_x2, a_y2 = [int(i) for i in input().split()]

b_x1, b_y1 = [int(i) for i in input().split()]
b_x2, b_y2 = [int(i) for i in input().split()]


if a_y1 < b_y2 or a_y2 > b_y1 or a_x2 < b_x1 or a_x1 > b_x2 :
    print("YES")
else:
    print("NO")