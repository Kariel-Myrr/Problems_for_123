y = int(input())
x = int(input())

# создаем начальные состояния
dp = []
for i in range(100):
    dp.append([0]*100)
dp[0][0] = 1

# начинаем с первого неопределенного состояния
for i in range(0, x):
    for j in range(0, y):
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]



# печатаем результат
print(dp[x - 1][y - 1])