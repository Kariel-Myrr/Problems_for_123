import math

n = int(input())

dists = []
x_prev, y_prev = [int(i) for i in input().split()]

for i in range(n - 1):
    x_cur, y_cur = [int(i) for i in input().split()]
    dists.append(math.sqrt((x_prev - x_cur) ** 2 + (y_prev - y_cur) ** 2))
    x_prev, y_prev = x_cur, y_cur

dp = [0, dists[0]]

for i in range(2, n):
    dp.append(min(dp[i-1] + dists[i], dp[i-1] + dists[i-1]))

print(dp[-1])