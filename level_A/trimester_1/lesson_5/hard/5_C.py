y = int(input())
x = int(input())

# создаем начальные состояния
dp = []
dp.append(1)  # добраться до начальной клетки 1 способ - остаться на ней
dp.append(1)  # добраться до 1-ой клетки 1 способ - 1 раз прыгнуть

if y == 2:
    dp[y - 1] = 0

# начинаем с первого неопределенного состояния
for i in range(2, x):

    if i == y - 1:
        dp.append(0)
        continue

    # задаем новое состояние
    new_point = dp[i - 1] + dp[i - 2]

    # немного места (см. след пункт)

    # добавляем его в массив
    dp.append(new_point)

# печатаем результат
print(dp[x - 1])
