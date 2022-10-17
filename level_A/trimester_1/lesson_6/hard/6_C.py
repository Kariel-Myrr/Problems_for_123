# Подсчет n-го числа фибоначчи ( аля fib(n) )

def my_fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    prev = 1
    cur = 1
    for i in range(2, n):
        buff = cur
        cur = cur + prev
        prev = buff

    return cur


a = int(input())
print(my_fib(a))
