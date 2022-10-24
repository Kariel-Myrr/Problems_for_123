

# Дана прямая и точка. Сказать ниже или выше прямой

a, b = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]

if y < a * x + b :
    print("lower")
else:
    print("higher")