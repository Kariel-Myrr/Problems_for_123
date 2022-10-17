# Дать массив чисел и запросы вида: вывести от,  до с таким то сепаратором


a = [i for i in input().split()]

n = int(input())

for i in range(n):
    from_, to_, sep_ = input().split(" ")
    from_ = int(from_)
    to_ = int(to_)

    print(sep_.join(a[from_: to_]))
