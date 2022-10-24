

# Дана последовательность точек - найти длину пути

n = int(input())

sum_ = 0
x_prev, y_prev = [int(i) for i in input().split()]

for i in range(n - 1) :
    x_cur, y_cur = [int(i) for i in input().split()]
    sum += math.sqrt((x_prev - x_cur) ** 2 + (y_prev - y_cur) ** 2)
    x_prev, y_prev = x_cur, y_cur

print(sum_)