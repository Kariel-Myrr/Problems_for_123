
x = int(input())

a = [1, 1, 2]

for i in range(3, x):

    t = a[i-1] + a[i-2] + a[i-3]

    a.append(t)

print(a[x-1])
