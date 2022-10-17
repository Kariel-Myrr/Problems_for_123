
# Создать массив от X до Y только с четными числами

x = int(input())
y = int(input())

a = []
for i in range(x, y+1):
    if i % 2 == 0:
        a.append(i)

print(a)
