# Минимум из 4-х чисел

def my_min_3(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c


def my_min_4(a, b, c, d):
    if a < b:
        return my_min_3(a, c, d)
    else:
        return my_min_3(b, c, d)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(my_min_4(a, b, c, d))
